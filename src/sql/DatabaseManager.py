from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from TableDefinition import DictionaryEntry


Base = declarative_base()
# TODO: CEDICT FILE LOCATION IMPORT
cedict_file = "../../res/data/cedict_ts.u8"


class DatabaseManager:
    engine = None

    def __init__(self, path):
        self.engine = create_engine(path, echo=True)
        Base.metadata.create_all(self.engine)


    def populate_database(self):
        session = Session(self.engine)
        inputFile = open(cedict_file)
        for line in inputFile:
            if line[0] == "#":
                continue
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
            new_word = DictionaryEntry(traditional, simplified, pinyin, english)
            session.add(new_word)
        session.commit()
