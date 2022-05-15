from PySide6.QtWidgets import QMenuBar, QFontDialog


class Menubar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.deposit_text = {"ENG": "Deposits", "PL": "Lokaty"}
        self.depositMenu = self.addAction(self.deposit_text[parent.language],
                                          lambda: self.parent().change_main_widget(self.deposit_text["ENG"]))
        self.bonds_text = {"ENG": "Bonds", "PL": "Obligacje"}
        self.bondsMenu = self.addAction(self.bonds_text[parent.language],
                                        lambda: self.parent().change_main_widget(self.bonds_text["ENG"]))
        self.stocks_text = {"ENG": "Stocks", "PL": "Akcje"}
        self.stocksMenu = self.addAction(self.stocks_text[parent.language],
                                         lambda: self.parent().change_main_widget(self.stocks_text["ENG"]))
        self.settings_text = {"ENG": "Settings", "PL" : "Ustawienia"}
        self.settingsMenu = self.addMenu(self.settings_text[parent.language])
        self.change_mode_text = {"dark": "light", "light": "dark"}
        self.changeModeAction = self.settingsMenu.addAction(self.change_mode_text[self.parent().mode] + " mode")
        self.change_font_text = {"ENG": "Change font", "PL" : "Zmień czcionkę"}
        self.changeFontAction = self.settingsMenu.addAction(self.change_font_text[self.parent().language])
        self.language_text = {"ENG": "Language", "PL": "Język"}
        self.languageMenu = self.addMenu(self.language_text[parent.language])
        self.englishAction = self.languageMenu.addAction("English")
        self.polskiAction = self.languageMenu.addAction("Polski")
        self.help_text = {"ENG": "Help", "PL": "Pomoc"}
        self.helpMenu = self.addMenu(self.help_text[parent.language])
        self.englishAction.triggered.connect(lambda: self.parent().change_all_widget_language("ENG"))
        self.polskiAction.triggered.connect(lambda: self.parent().change_all_widget_language("PL"))
        self.changeModeAction.triggered.connect(self.change_mode)
        self.changeFontAction.triggered.connect(self.change_font)

    def set_language(self):
        self.depositMenu.setText(self.deposit_text[self.parent().language])
        self.bondsMenu.setText(self.bonds_text[self.parent().language])
        self.stocksMenu.setText(self.stocks_text[self.parent().language])
        self.settingsMenu.setTitle(self.settings_text[self.parent().language])
        self.changeFontAction.setText(self.change_font_text[self.parent().language])
        self.languageMenu.setTitle(self.language_text[self.parent().language])
        self.helpMenu.setTitle(self.help_text[self.parent().language])

    def change_mode(self):
        self.parent().mode = self.change_mode_text[self.parent().mode]
        self.parent().set_mode()
        self.changeModeAction.setText(self.change_mode_text[self.parent().mode] + " mode")

    def change_font(self):
        status, font = QFontDialog.getFont()
        if status:
            self.parent().change_all_widget_font(font)
