from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

from Menubar import Menubar
from DepositWidget import DepositWidget
from BondsWidget import BondsWidget
from StocksWidget import StocksWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.language = "ENG"
        self.mode = "dark"
        self.mode_dict = {"dark": (53, Qt.white), "light": (240, Qt.black)}
        self.main_widget_dict = {"Deposits": DepositWidget,
                                 "Bonds": BondsWidget,
                                 "Stocks": StocksWidget}
        self.setWindowTitle("Investment Calculator")
        self.setMenuBar(Menubar(self))
        self.setCentralWidget(DepositWidget(self))
        self.set_mode()

    def set_mode(self):
        # color values are in rgb from 0 to 255, all colors 0 - black, all 255 - white
        red = self.mode_dict[self.mode][0]
        green = self.mode_dict[self.mode][0]
        blue = self.mode_dict[self.mode][0]
        text_color = self.mode_dict[self.mode][1]
        color_correct = {"dark": 25, "light": -15}
        correct = color_correct[self.mode]
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(red, green, blue))
        palette.setColor(QPalette.WindowText, text_color)
        palette.setColor(QPalette.Base, QColor(red - correct, green - correct, blue - correct))
        palette.setColor(QPalette.Text, text_color)
        palette.setColor(QPalette.Button, QColor(red, green, blue))
        palette.setColor(QPalette.ButtonText, text_color)
        self.setPalette(palette)

    def change_main_widget(self, widget_name):
        main_widget = self.main_widget_dict[widget_name](self)
        self.setCentralWidget(main_widget)
        self.setFixedSize(0, 0)

    def change_all_widget_font(self, font):
        self.setFont(font)

    def change_all_widget_language(self, language):
        self.language = language
        children_list = self.children()
        for children in children_list:
            try:
                children.set_language()
            except AttributeError:
                continue


def main():
    app = QApplication([])
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
