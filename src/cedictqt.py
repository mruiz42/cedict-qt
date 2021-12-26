from PyQt5.QtWidgets import QApplication
from os.path import exists
import sys
from src.callMainWindow import MainWindow
from src.ConfigManager import ConfigManager
from src.sql.DatabaseManager import DatabaseManager




if __name__ == "__main__":
    config_man = ConfigManager()              # Initialize the Config Manager
    database_man = DatabaseManager(config_man.getDatabasePath())
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    exit(app.exec_())
