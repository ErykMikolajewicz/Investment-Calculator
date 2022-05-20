from PySide6.QtWidgets import QMenuBar, QFontDialog


class Menubar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.deposit_text = {"ENG": "Deposits",
                             "PL": "Lokaty"}
        deposit_index = 0
        self.depositMenu = self.addAction(self.deposit_text[parent.language],
                                          lambda: self.parent().set_main_widget(deposit_index))
        self.bonds_text = {"ENG": "Bonds",
                           "PL": "Obligacje"}
        bonds_index = 1
        self.bondsMenu = self.addAction(self.bonds_text[parent.language],
                                        lambda: self.parent().set_main_widget(bonds_index))
        self.stocks_text = {"ENG": "Stocks",
                            "PL": "Akcje"}
        stocks_index = 2
        self.stocksMenu = self.addAction(self.stocks_text[parent.language],
                                         lambda: self.parent().set_main_widget(stocks_index))


        self.settings_text = {"ENG": "Settings",
                              "PL": "Ustawienia"}
        self.settingsMenu = self.addMenu(self.settings_text[parent.language])

        self.change_mode_text = {"dark": "light",
                                 "light": "dark"}
        self.changeModeAction = self.settingsMenu.addAction(self.change_mode_text[self.parent().mode] + " mode")
        self.changeModeAction.triggered.connect(self.change_mode)

        self.change_font_text = {"ENG": "Change font",
                                 "PL": "Zmień czcionkę"}
        self.changeFontAction = self.settingsMenu.addAction(self.change_font_text[self.parent().language])
        self.changeFontAction.triggered.connect(self.change_font)


        self.language_text = {"ENG": "Language",
                              "PL": "Język"}
        self.languageMenu = self.addMenu(self.language_text[parent.language])

        self.englishAction = self.languageMenu.addAction("English")
        self.englishAction.triggered.connect(lambda: self.parent().set_widgets_language("ENG"))

        self.polskiAction = self.languageMenu.addAction("Polski")
        self.polskiAction.triggered.connect(lambda: self.parent().set_widgets_language("PL"))


        self.help_text = {"ENG": "Help",
                          "PL": "Pomoc"}
        self.helpMenu = self.addMenu(self.help_text[parent.language])

    def set_language(self, language):
        self.depositMenu.setText(self.deposit_text[language])
        self.bondsMenu.setText(self.bonds_text[language])
        self.stocksMenu.setText(self.stocks_text[language])
        self.settingsMenu.setTitle(self.settings_text[language])
        self.changeFontAction.setText(self.change_font_text[language])
        self.languageMenu.setTitle(self.language_text[language])
        self.helpMenu.setTitle(self.help_text[language])

    def change_mode(self):
        self.parent().mode = self.change_mode_text[self.parent().mode]
        self.parent().set_mode()
        self.changeModeAction.setText(self.change_mode_text[self.parent().mode] + " mode")

    def change_font(self):
        status, font = QFontDialog.getFont()
        if status:
            self.parent().change_all_widget_font(font)
