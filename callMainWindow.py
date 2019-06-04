from MainWindow import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
import re
from random import randint
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = QSqlDatabase.addDatabase("QSQLITE", "SQLITE")
        self.db.setDatabaseName("dictionary.db")
        self.db.open()
        print(self.db.lastError())
        self.model = QSqlQueryModel()
        self.model.setQuery("SELECT * FROM WORD_LIST", self.db)

        # self.tab = QSqlTableModel(self.ui.tableView, self.db)
        # self.tab.setTable("WORD_LIST")
        # self.tab.setEditStrategy(QSqlTableModel.OnFieldChange)
        # self.tab.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0,True)
        self.ui.tableView.clicked.connect(self.getRowData)
        self.ui.tableView.setColumnWidth(4, 80)
        self.ui.tableView.setColumnWidth(4, 320)
        self.ui.lineEdit_query.textChanged.connect(self.queryAction)
        # self.ui.tableView.
        self.ui.pushButton_search.clicked.connect(self.queryAction)
        numRows = self.model.rowCount()
        self.ui.tableView.selectRow(randint(0, numRows))
        self.getRowData()
        # self.ui.tableView.itemChanged.connect(self.queryAction)
        # self.ui.tableView.
        self.show()

    def queryAction(self):
        queryWord = self.ui.lineEdit_query.text()
        command = ("SELECT * FROM WORD_LIST WHERE ENGLISH LIKE \"%" + queryWord + "%\""
                   "OR SIMPLIFIED LIKE \"%" + queryWord + "%\""
                   "OR TRADITIONAL LIKE \"%" + queryWord + "%\""
                   "OR PINYIN LIKE \"%" + queryWord + "%\"")
        print(command)
        self.model.setQuery(command, self.db)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.selectRow(0)
        self.getRowData()
    def getRowData(self):

        index = self.ui.tableView.currentIndex()
        row = index.row()
        t = index.sibling(row, 1).data()
        s = index.sibling(row, 2).data()
        p = index.sibling(row, 3).data()
        e = index.sibling(row, 4).data()
        defList = e.split("/")
        e = ""
        for i in range (0, len(defList)):
            e += str((i+1)) + ". " + defList[i] + "\n"
        n = decode_pinyin(p)
        self.ui.label_hanzi.setText(t + "\n" + s)
        self.ui.label_pinyin.setText(n)
        self.ui.label_english.setText(e)



PinyinToneMark = {
    0: "aoeiuv\u00fc",
    1: "\u0101\u014d\u0113\u012b\u016b\u01d6\u01d6",
    2: "\u00e1\u00f3\u00e9\u00ed\u00fa\u01d8\u01d8",
    3: "\u01ce\u01d2\u011b\u01d0\u01d4\u01da\u01da",
    4: "\u00e0\u00f2\u00e8\u00ec\u00f9\u01dc\u01dc",
}

def decode_pinyin(s):
    s = s.lower()
    r = ""
    t = ""
    for c in s:
        if c >= 'a' and c <= 'z':
            t += c
        elif c == ':':
            assert t[-1] == 'u'
            t = t[:-1] + "\u00fc"
        else:
            if c >= '0' and c <= '5':
                tone = int(c) % 5
                if tone != 0:
                    m = re.search("[aoeiuv\u00fc]+", t)
                    if m is None:
                        t += c
                    elif len(m.group(0)) == 1:
                        t = t[:m.start(0)] + PinyinToneMark[tone][PinyinToneMark[0].index(m.group(0))] + t[m.end(0):]
                    else:
                        if 'a' in t:
                            t = t.replace("a", PinyinToneMark[tone][0])
                        elif 'o' in t:
                            t = t.replace("o", PinyinToneMark[tone][1])
                        elif 'e' in t:
                            t = t.replace("e", PinyinToneMark[tone][2])
                        elif t.endswith("ui"):
                            t = t.replace("i", PinyinToneMark[tone][3])
                        elif t.endswith("iu"):
                            t = t.replace("u", PinyinToneMark[tone][4])
                        else:
                            t += "!"
            r += t
            t = ""
    r += t
    return r

if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()

    exit(app.exec_())