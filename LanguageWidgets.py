from PySide6.QtWidgets import QLabel, QComboBox, QPushButton, QErrorMessage


class LLabel(QLabel):
    def __int__(self):
        super().__init__()
        self.language_versions = {}

    def set_language(self, language):
        self.setText(self.language_versions[language])


class LComboBox(QComboBox):
    def __int__(self):
        super().__init__()
        self.language_versions = {}

    def set_language(self, language):
        self.clear()
        self.addItems(self.language_versions[language])


class LPushButton(QPushButton):
    def __int__(self):
        super().__init__()
        self.language_versions = {}

    def set_language(self, language):
        self.setText(self.language_versions[language])


class LErrorMessage(QErrorMessage):
    def __int__(self):
        super().__init__()
        self.language_versions = {}

    def set_language(self, language):
        self.setText(self.language_versions[language])
