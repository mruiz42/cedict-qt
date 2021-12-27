# import sqlite3
#
#
# class DictWord:
#     def __init__(self, t: str, s: str, p: str, e: list):
#         self.traditional = t
#         self.simplified = s
#         self.pinyin = p
#         self.english = e
#
#
# inputFile = open("cedict_ts.u8", mode='r')
#
# wordList = []
# db = sqlite3.connect("dictionary.db")
# cur = db.cursor()
# command = ("CREATE TABLE IF NOT EXISTS WORD_LIST "
#            "(CARD_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
#            "TRADITIONAL TEXT, "
#            "SIMPLIFIED TEXT, "
#            "PINYIN TEXT,"
#            "ENGLISH TEXT);")
# db.execute(command)
#
# for line in inputFile:
#     # e = []
#     if line[0] == "#":
#         continue
#     hanziPos = line.find("[")
#     hanziList = line[:hanziPos].split(" ")
#     t = hanziList[0]
#     s = hanziList[1]
#     pinyinPos = line.find("]")
#     p = line[hanziPos:pinyinPos].strip("[]")
#     englishPos = line.find("/")
#     e = line[englishPos + 1:-2]  # .split("/")
#     # for i in englishList:
#     #   e.append(i)
#     inputSet = (t, s, p, e)
#     command = "INSERT INTO WORD_LIST (TRADITIONAL, SIMPLIFIED, PINYIN, ENGLISH) VALUES (?, ?, ?, ?);"
#     db.execute(command, inputSet)
# db.commit()
# tempWord = DictWord(t, s, p, e)
# wordList.append(tempWord)
