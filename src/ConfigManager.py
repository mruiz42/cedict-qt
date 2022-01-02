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

    def getStr(self, section: str, key: str) -> str:
        return self.config[section].get(key)

    def getBool(self, section: str, key: str) -> bool:
        return self.config[section].getboolean(key)

    def getDatabasePath(self) -> str:
        return self.config[self.section].get("SQLALCHEMY_DATABASE_PATH")

    def getStartRandomized(self) -> bool:
        return self.config.getboolean(self.section, "START_RANDOMIZED")

    def getShowAll(self) -> bool:
        return self.config.getboolean(self.section, "SHOW_ALL")

    def getShowTraditional(self) -> bool:
        return self.config.getboolean(self.section, "SHOW_TRADITIONAL")

    def getShowSimplified(self) -> bool:
        return self.config.getboolean(self.section, "SHOW_SIMPLIFIED")

    def getShowPinyin(self) -> bool:
        return self.config.getboolean(self.section, "SHOW_PINYIN")

    def set(self, section: str, key: str, val: str) -> bool:
        """
        Updates a specific key in the configuration file to a given value.
        Note that commit must be called to write changes to config file!
        :param section: The section in the configuration file. eg: DEBUG, INSTALL, PORTABLE
        :param key: The key to be updated.
        :param val: The new desired value.
        :return: Returns True on success.
        """
        try:
            self.config.set(self.section, key, val)
            return True
        except ConfigParser.NoSectionError:
            # TODO: Consider raising a new exception here for code portability
            return False

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