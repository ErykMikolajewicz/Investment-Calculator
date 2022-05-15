from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel


class StocksWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.not_implemented_label = QLabel("Not implemented")
        self.not_implemented_label.setFixedSize(400, 200)
        layout = QGridLayout()
        layout.addWidget(self.not_implemented_label, 3, 3, Qt.AlignVCenter | Qt.AlignHCenter)
        self.setLayout(layout)


    def set_language(self):
        pass