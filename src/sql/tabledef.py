from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

# DATABASE TABLE DEFINITIONS ###############################################
class DictionaryEntry(Base):
    """

    """
    __tablename__ = "dictionary_entry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    traditional = Column(String)
    simplified = Column(String)
    pinyin = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, traditional: str, simplified: str, pinyin: str, english: str):
        """

        """
        self.traditional = traditional
        self.simplified = simplified
        self.pinyin = pinyin
        self.english = english


class ApplicationMeta(Base):
    """

    """
    __tablename__ = "application_meta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    program_version = Column(String)
    database_version = Column(String)
    cedict_version = Column(String)
    db_creation_time = Column(DateTime)
    cedict_creation_time = Column(DateTime)
    entries = Column(Integer)
    cedict_license = Column(String)
    cedict_publisher = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, program_version: str, database_version: str, cedict_version: str,
                 db_creation_time: datetime, cedict_creation_time: datetime,
                 entries: int, cedict_license: str, cedict_publisher: str):
        self.program_version = program_version  # TODO: Change to application_version for consistency
        self.database_version = database_version
        self.cedict_version = cedict_version
        self.db_creation_time = db_creation_time
        self.cedict_creation_time = cedict_creation_time
        self.entries = entries
        self.cedict_license = cedict_license
        self.cedict_publisher = cedict_publisher
