import sys

from src import ConfigManager
from src.sql import DatabaseManager
from src.ui.MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import re
# from gtts import gTTS
from random import randint


# from playsound import playsound
# import simpleaudio as sa
# from pydub import AudioSegment


class MainWindow(QMainWindow):
    db_mgr = None           # Database manager object
    cfg_mgr = None          # Configuration manager object
    ui = None               # MainWindow object
    db = None               # Database connection for making raw sql queries
    model = None            # QSqlQueryModel object
    table = None            # QSqlTableModel object
    selection = None        # Selected entry in the database

    def __init__(self, database_mgr: DatabaseManager, config_mgr: ConfigManager):
        super().__init__()
        self.db_mgr = database_mgr
        self.cfg_mgr = config_mgr
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # TODO: TTS Broken, pls fix
        # self.tts = gTTS("nihao", "zh-cn")
        # self.s = ""
        # self.mp3_fp = BytesIO()
        self._setup_preferences()
        self._setup_database_conn()
        self._setup_table()
        self._setup_actions()
        self._preload_random_entry()
        # self.ui.pushButton_audio.clicked.connect(self.playButtonAction)
        self.getRowData()
        self.show()

    def _preload_random_entry(self):
        self.ui.tableView.selectRow(randint(0, self.model.rowCount()))

    def _setup_database_conn(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE", "SQLITE")
        self.db.setDatabaseName(self.db_mgr.get_db_path())
        self.db.open()

    def _setup_table(self):
        self.model = QSqlQueryModel()
        self.model.setQuery(self.db_mgr.get_all_dictionary_entries_stmt(), self.db)
        self.table = QSqlTableModel(self.ui.tableView, self.db)
        self.table.setTable("dictionary_entry")
        self.table.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.table.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.clicked.connect(self.getRowData)
        self.ui.tableView.setColumnWidth(3, 80)
        self.selection = self.ui.tableView.selectionModel()


    def _setup_actions(self):
        self.ui.lineEdit_query.textChanged.connect(self.queryAction)
        self.ui.pushButton_search.clicked.connect(self.queryAction)
        self.selection.selectionChanged.connect(self.getRowData)

    def _setup_preferences(self):
        # Setup column menu actions
        is_show_traditional = self.cfg_mgr.getShowTraditional()
        is_show_simplified = self.cfg_mgr.getShowSimplified()
        is_show_pinyin = self.cfg_mgr.getShowPinyin()
        self.ui.actionTraditional.setChecked(is_show_traditional)
        self.ui.actionSimplified.setChecked(is_show_simplified)
        self.ui.actionPinyin.setChecked(is_show_pinyin)
        if is_show_pinyin and is_show_traditional and is_show_simplified:
            self.ui.actionAll.setChecked(True)
        else:
            self.ui.actionAll.setChecked(False)
        # Action listeners
        self.ui.actionExit.triggered.connect(self._signal_exit)
        self.ui.actionAll.triggered.connect(self._signal_toggleShowAll)
        self.ui.actionPinyin.triggered.connect(self._signal_toggleShowPinyin)
        self.ui.actionSimplified.triggered.connect(self._signal_toggleShowSimplified)
        self.ui.actionTraditional.triggered.connect(self._signal_toggleShowTraditional)

    def playButtonAction(self) -> None:
        """
        ** DEPRECIATED **
        This function no longer works
        :return: Nothing.
        """
        # self.tts = gTTS(self.s, "zh-cn")
        # self.tts.save("out.mp3")
        # sound = AudioSegment.from_mp3("out.mp3")
        # sound.export("out.wav", format="wav")
        # wave_obj = sa.WaveObject.from_wave_file("out.wav")
        # play_obj = wave_obj.play()
        # play_obj.wait_done()
        # print(self.s, "Audio played")
        pass

    def queryAction(self):
        queryWord = self.ui.lineEdit_query.text()
        command = ("SELECT * FROM DICTIONARY WHERE ENGLISH LIKE \"%" + queryWord + "%\""
                   "OR SIMPLIFIED LIKE \"%" + queryWord + "%\""
                   "OR TRADITIONAL LIKE \"%" + queryWord + "%\""
                   "OR PINYIN LIKE \"%" + queryWord + "%\"")
        self.model.setQuery(command, self.db)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.selectRow(0)
        self.getRowData()

    def getRowData(self):
        index = self.ui.tableView.currentIndex()
        row = index.row()
        self.s = index.sibling(row, 2).data()
        traditional = index.sibling(row, 1).data()
        simplified = index.sibling(row, 2).data()
        pinyin = index.sibling(row, 3).data()
        definition = index.sibling(row, 4).data()
        defList = definition.split("/")
        defList = definition.split("/")
        definition = ""
        for i in range (0, len(defList)):
            definition += str((i+1)) + ". " + defList[i] + "\n"
        n = decode_pinyin(pinyin)
        self.ui.label_hanzi_traditional.setText(traditional)
        self.ui.label_hanzi_simplified.setText(simplified)
        self.ui.label_pinyin.setText(n)
        self.ui.label_definition.setText(definition)

    def _signal_toggleShowAll(self):
        # TODO: This doesnt really work
        current_state = self.ui.actionAll.isChecked()
        self.ui.actionAll.setChecked(current_state)
        self.ui.actionSimplified.setChecked(current_state)
        self.ui.actionTraditional.setChecked(current_state)
        self.ui.actionPinyin.setChecked(current_state)
        current_state = not current_state
        self.ui.label_pinyin.setHidden(current_state)
        self.ui.tableView.setColumnHidden(3, current_state)
        self.ui.groupbox_traditional.setHidden(current_state)
        self.ui.tableView.setColumnHidden(1, current_state)
        self.ui.groupBox_simplified.setHidden(current_state)
        self.ui.tableView.setColumnHidden(2, current_state)

    def _signal_toggleShowPinyin(self):
        current_state = self.ui.label_pinyin.isHidden()
        self.ui.label_pinyin.setHidden(not current_state)
        self.ui.tableView.setColumnHidden(3, not current_state)

    def _signal_toggleShowTraditional(self):
        current_state = self.ui.label_hanzi_traditional.isHidden()
        self.ui.groupbox_traditional.setHidden(not current_state)
        self.ui.tableView.setColumnHidden(1, not current_state)

    def _signal_toggleShowSimplified(self):
        current_state = self.ui.label_hanzi_simplified.isHidden()
        self.ui.groupBox_simplified.setHidden(not current_state)
        self.ui.tableView.setColumnHidden(2, not current_state)


    def _signal_exit(self):
        sys.exit(0)

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