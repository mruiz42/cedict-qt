# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Tue Jun  4 13:50:32 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 720)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_query = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_query.setObjectName("lineEdit_query")
        self.horizontalLayout_2.addWidget(self.lineEdit_query)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_2.addWidget(self.pushButton_search)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tableView)
        self.Hanzi = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hanzi.sizePolicy().hasHeightForWidth())
        self.Hanzi.setSizePolicy(sizePolicy)
        self.Hanzi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Hanzi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Hanzi.setObjectName("Hanzi")
        self.gridLayout = QtWidgets.QGridLayout(self.Hanzi)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.label_english = QtWidgets.QLabel(self.Hanzi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_english.sizePolicy().hasHeightForWidth())
        self.label_english.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_english.setFont(font)
        self.label_english.setScaledContents(True)
        self.label_english.setWordWrap(True)
        self.label_english.setIndent(-1)
        self.label_english.setObjectName("label_english")
        self.gridLayout.addWidget(self.label_english, 4, 1, 1, 2)
        self.label_pinyin = QtWidgets.QLabel(self.Hanzi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pinyin.sizePolicy().hasHeightForWidth())
        self.label_pinyin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(36)
        self.label_pinyin.setFont(font)
        self.label_pinyin.setScaledContents(True)
        self.label_pinyin.setWordWrap(True)
        self.label_pinyin.setObjectName("label_pinyin")
        self.gridLayout.addWidget(self.label_pinyin, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.label_hanzi = QtWidgets.QLabel(self.Hanzi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_hanzi.sizePolicy().hasHeightForWidth())
        self.label_hanzi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(42)
        self.label_hanzi.setFont(font)
        self.label_hanzi.setScaledContents(True)
        self.label_hanzi.setWordWrap(True)
        self.label_hanzi.setObjectName("label_hanzi")
        self.gridLayout.addWidget(self.label_hanzi, 0, 1, 1, 2)
        self.pushButton_audio = QtWidgets.QPushButton(self.Hanzi)
        self.pushButton_audio.setObjectName("pushButton_audio")
        self.gridLayout.addWidget(self.pushButton_audio, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.Hanzi)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lineEdit_query.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Enter a search query...", None, -1))
        self.pushButton_search.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.label_english.setText(QtWidgets.QApplication.translate("MainWindow", "Definition", None, -1))
        self.label_pinyin.setText(QtWidgets.QApplication.translate("MainWindow", "Pinyin", None, -1))
        self.label_hanzi.setText(QtWidgets.QApplication.translate("MainWindow", "Hanzi", None, -1))
        self.pushButton_audio.setText(QtWidgets.QApplication.translate("MainWindow", "Audio", None, -1))

