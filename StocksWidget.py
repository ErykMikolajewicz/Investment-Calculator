from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QTableWidget


class StocksWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.not_implemented_label = QLabel("Not implemented")
        self.not_implemented_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.not_implemented_label.setFixedSize(400, 200)
        layout = QGridLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        layout.addWidget(self.not_implemented_label, 0, 0)
        #layout.addWidget(self.tableWidget, 1, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        self.setLayout(layout)

    def set_language(self):
        pass