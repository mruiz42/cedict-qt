from configparser import ConfigParser

# TODO this should be stored in different locations based on Operating System
CONFIG_URI = "../res/config/cedictqt.conf"


class ConfigManager:
    config = None
    section = None
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_URI)
        self.section = "DEBUG"  # TODO: Change this for release build

    # Getters
    def getSection(self):
        return self.section

    def getStr(self, key: str) -> str:
        return self.config[self.section].get(key)

    def getBool(self, key: str) -> bool:
        return self.config[self.section].getboolean(key)

    def getInt(self, key: str) -> int:
        return self.config[self.section].getint(key)

    def getDatabasePath(self) -> str:
        return self.config[self.section].get("sqlalchemy_database_path")

    def getStartRandomized(self) -> bool:
        return self.config.getboolean(self.section, "start_randomized")

    def getShowAll(self) -> bool:
        return self.config.getboolean(self.section, "show_all")

    def getShowTraditional(self) -> bool:
        return self.config.getboolean(self.section, "show_traditional")

    def getShowSimplified(self) -> bool:
        return self.config.getboolean(self.section, "show_simplified")

    def getShowPinyin(self) -> bool:
        return self.config.getboolean(self.section, "show_pinyin")

    def getShowEnglish(self) -> bool:
        return self.config.getboolean(self.section, "show_english")

    def set(self, key: str, val: str) -> bool:
        """
        Updates a specific key in the configuration file to a given value.
        Note that commit must be called to write changes to config file!
        :param key: The key to be updated.
        :param val: The new desired value.
        :return: Returns True on success.
        """

        self.config.set(self.section, key, val)
        return True
    def setNow(self, section: str, key: str, val: str) -> bool:
        """
        Helper method for set() with autocommit
        Updates a specific key in the configuration file to a given value.
        :param section: The section in the configuration file. eg: DEBUG, INSTALL, PORTABLE
        :param key: The key to be updated.
        :param val: The new desired value.
        :return: Returns True on success.
        """
        self.set(section, key, val)
        self.commit()
        return True     # TODO: exception handling

    def commit(self) -> bool:
        """
        Writes any changes to the config file.
        :return: None
        """
        # TODO: Exception handling
        with open(CONFIG_URI, 'w') as cfg_file:
            self.config.write(cfg_file)
            return True


#         # for key in ["SHOW_ALL", "SHOW_PINYIN", "SHOW_TRADITIONAL", "SHOW_SIMPLIFIED"]:
#         #     self.cfg_mgr.set(self.cfg_mgr.getSection(), key, str(not current_state))