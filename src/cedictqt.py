from PyQt5.QtWidgets import QApplication
from os.path import exists
import sys
from src.callMainWindow import MainWindow
from src.ConfigManager import ConfigManager
from src.sql.DatabaseManager import DatabaseManager


def initialize_db():
    pass


def check_db():
    if not (exists(config_man.getDatabaseUri())):
        print(config_man.getDatabaseUri())
        initialize_db()


if __name__ == "__main__":
    config_man = ConfigManager()              # Initialize the Config Manager
    check_db()
    database_man = DatabaseManager(config_man.getDatabaseUri())
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    exit(app.exec_())
