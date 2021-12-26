from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


# DATABASE TABLE DEFINITIONS ###############################################
class DictionaryEntry(Base):
    """

    """
    __tablename__ = "dictionary_word"
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

Base.metadata.create_all(engine)
