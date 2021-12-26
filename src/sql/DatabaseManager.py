import os.path
from urllib.request import urlretrieve
import tempfile
from datetime import datetime
from os.path import exists
from zipfile import ZipFile

from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

from src.sql.tabledef import DictionaryEntry as Entry, ApplicationMeta as Meta, Base

# TODO: CEDICT FILE LOCATION IMPORT
cedict_file = "./res/data/cedict_ts.u8"
# TODO: Centralize location for program version
PROGRAM_VER = "0.2"
DATABASE_VER = "0.1"


class DatabaseManager:
    db_path = None
    _sql_engine = None
    _uri = None
    _application_metadata = None
    def __init__(self, path: str): # TODO: DETERMINE IF DATABASE INTEGRITY EXIST
        """
        :param path: The path of the sqlite3 database file.
        """
        self.db_path = path
        # TODO: Detect if path absolute or relative to determine if 3 or 4 slashes are needed
        self._uri = "sqlite:///" + path
        self._sql_engine = create_engine(self._uri, echo=True)

        # TODO: DB Integrity check
        if not (self._db_exists() or self._get_db_metadata() == None):
            Base.metadata.create_all(self._sql_engine)
            self._populate_database()
        else:
            self._application_metadata = self._get_db_metadata()
            if (self._application_metadata == None):
                print("Error fetching database metadata. Something went wrong... Aborting!")
                exit(100)
                # TODO: Handle this case better
            else:
                print("Database version", self._application_metadata.program_version)


    def _get_db_metadata(self) -> Meta:
        session = Session(self._sql_engine)
        obj = None
        try:
            # https://stackoverflow.com/questions/8551952/how-to-get-last-record
            metadata = session.query(Meta).order_by(Meta.id.desc()).first()
        except:
            print("Error getting metadata")
        session.close()
        return metadata

    def _db_exists(self) -> bool:
        return exists(self.db_path)

    def _populate_database(self) -> bool:
        session = Session(self._sql_engine)
        cedict_file = self._get_cedict_file()
        inputFile = open(cedict_file)
        metadata = dict()
        num_entries = 0
        for line in inputFile:
            if line[0] == "#":
                if line[1] == "!":
                    # "#!" is the denotation for ce-dict metadata
                    line = line.lstrip("#! ")
                    line = line.rstrip(" \n")
                    meta_part = line.split("=")
                    metadata[meta_part[0]] = meta_part[1]
            else:
                hanziPos = line.find("[")
                hanziList = line[:hanziPos].split(" ")
                traditional = hanziList[0]
                simplified = hanziList[1]
                pinyinPos = line.find("]")
                pinyin = line[hanziPos:pinyinPos].strip("[]")
                englishPos = line.find("/")
                english = line[englishPos + 1:-2]  # .split("/")
                # for i in englishList:
                #   e.append(i)
                new_word = Entry(traditional, simplified, pinyin, english)
                session.add(new_word)
                num_entries += 1
                # if (num_entries % 1000 == 0):
                #     session.commit() # commit every 1000 entries
        session.commit()
        # insert metadata
        program_version = PROGRAM_VER
        database_version = DATABASE_VER
        cedict_version = metadata["version"] + "." + metadata["subversion"]
        db_creation_time = datetime.utcnow()
        cedict_creation_time = metadata["date"].strip("Z")
        cedict_creation_time = datetime.fromisoformat(cedict_creation_time)
        entries = int(metadata["entries"])
        cedict_license = metadata["license"]
        cedict_publisher = metadata["publisher"]
        new_meta = Meta(program_version, database_version, cedict_version,
                        db_creation_time, cedict_creation_time, entries,
                        cedict_license, cedict_publisher)
        session.add(new_meta)
        session.commit()
        session.close()
        return True

    def _get_cedict_file(self) -> str:
        temp_dir = tempfile.mkdtemp(prefix="cedict-qt_")
        file_dest = tempfile.mkstemp(dir=temp_dir)
        cc_cedict_url = "https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip"
        urlretrieve(cc_cedict_url, file_dest[1])
        filelist = None
        with ZipFile(file_dest[1]) as z:
            filelist = z.namelist()
            z.extractall(temp_dir)
        cedict_path = os.path.join(temp_dir, "cedict_ts.u8")
        # os.path.isfile(cedict_path)
        # TODO: Handle deletion of temporary files
        # os.removedirs(temp_dir)
        return cedict_path

