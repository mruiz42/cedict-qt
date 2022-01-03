from src.ui.PreferencesDialog import *
from src.ConfigManager import ConfigManager as cm

class PreferencesDialog(QtWidgets.QDialog):
    parent = None
    cfg_mgr = None
    cached_vals = None

    def __init__(self, cfg_mgr: cm, parent=None):
        super(PreferencesDialog, self).__init__(parent)
        self.parent = parent
        self.dialog = Ui_Dialog()
        self.cfg_mgr = cfg_mgr
        self.cached_vals = dict()
        self.dialog.setupUi(self)
        self._preloadValues()
        print(self.dialog.buttonBox.buttons())

    def _setup_actions(self):
        # TODO: Not sure how to better access dialog buttons
        buttons = self.dialog.buttonBox.buttons()
        revert_btn = buttons[0]
        apply_btn = buttons[1]
        cancel_btn = buttons[2]
        apply_btn.clicked(self._action_applyChanges)
        # self.dialog.buttonBox.button("Apply").(self._action_applyChanges)
        self.dialog.buttonBox.rejected(self._action_applyChanges)

    def _preloadValues(self):
        self.cached_vals["sqlalchemy_database_path"] = self.cfg_mgr.getDatabasePath()
        self.cached_vals["start_randomized"] = self.cfg_mgr.getStartRandomized()
        self.cached_vals["show_english"] = self.cfg_mgr.getShowEnglish()
        self.cached_vals["show_traditional"] = self.cfg_mgr.getShowTraditional()
        self.cached_vals["show_simplified"] = self.cfg_mgr.getShowSimplified()
        self.cached_vals["show_pinyin"] = self.cfg_mgr.getShowPinyin()
        # set checkbox values
        self.dialog.checkBox_randomStartup.setChecked(self.cached_vals["start_randomized"])
        self.dialog.checkBox_displayEnglish.setChecked(self.cached_vals["show_english"])
        self.dialog.checkBox_displayPinyin.setChecked(self.cached_vals["show_pinyin"])
        self.dialog.checkBox_displayTraditional.setChecked(self.cached_vals["show_traditional"])
        self.dialog.checkBox_displaySimplified.setChecked(self.cached_vals["show_simplified"])
        self.dialog.lineEditDatabasePath.setText(self.cached_vals["sqlalchemy_database_path"])

    def _action_applyChanges(self):
        db_path = self.dialog.checkBox_randomStartup.isChecked()
        start_randomized = self.dialog.checkBox_randomStartup.isChecked()
        show_english = self.dialog.checkBox_displayEnglish.isChecked()
        show_traditional = self.dialog.checkBox_displayTraditional.isChecked()
        show_simplified = self.dialog.checkBox_displaySimplified.isChecked()
        show_english = self.dialog.checkBox_displayEnglish.isChecked()
        show_pinyin = self.dialog.checkBox_displayPinyin.isChecked()
        # TODO: Validate database path
        self.cfg_mgr.set("sqlalchemy_database_path", db_path)
        self.cfg_mgr.set("start_randomized", start_randomized)
        self.cfg_mgr.set("show_english", show_english)
        self.cfg_mgr.set("show_traditional", show_traditional)
        self.cfg_mgr.set("show_simplified", show_simplified)
        self.cfg_mgr.set("show_pinyin", show_pinyin)
        self.cfg_mgr.commit()


    # def _action_revertChanges(self):

