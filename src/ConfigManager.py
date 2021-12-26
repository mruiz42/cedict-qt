from configparser import ConfigParser


# TODO this should be stored in different locations based on Operating System
CONFIG_URI = "../res/config/cedictqt.conf"


class ConfigManager:
    config = None

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_URI)

    def getDatabaseUri(self) -> str:
        return self.config["DEBUG"].get("SQLALCHEMY_DATABASE_URI")

