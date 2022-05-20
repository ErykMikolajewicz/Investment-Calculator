from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSizePolicy
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

from Menubar import Menubar
from DepositWidget import DepositWidget
from BondsWidget import BondsWidget
from StocksWidget import StocksWidget


class InvestmentCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Investment Calculator")
        self.language = "ENG"
        self.mode = "dark"
        self.mode_dict = {"dark": (53, Qt.white), "light": (240, Qt.black)}
        self.setMenuBar(Menubar(self))
        self.stackWidget = QStackedWidget()
        self.stackWidget.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)  # stackWidget hints don't work correct
        self.setCentralWidget(self.stackWidget)
        self.depositWidget = DepositWidget()
        self.bondsWidget = BondsWidget()
        self.stocksWidget = StocksWidget()
        self.stackWidget.addWidget(self.depositWidget)
        self.stackWidget.addWidget(self.bondsWidget)
        self.stackWidget.addWidget(self.stocksWidget)
        self.set_main_widget(self.stackWidget.currentIndex())
        self.set_widgets_language(self.language)
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

    # function also repair not working size hints from stackWidget
    def set_main_widget(self, widget_index):
        self.stackWidget.setCurrentWidget(self.stackWidget.widget(widget_index))
        current_geometry = self.geometry()
        x_coordinate, y_coordinate = current_geometry.x(), current_geometry.y()
        main_widget_size = self.stackWidget.currentWidget().sizeHint()
        other_widget_size = self.sizeHint()
        new_widget_width = main_widget_size.width() + other_widget_size.width()
        new_widget_height = main_widget_size.height() + other_widget_size.height()
        self.setGeometry(x_coordinate, y_coordinate, new_widget_width, new_widget_height)

    def change_all_widget_font(self, font):
        self.setFont(font)
        self.set_main_widget(self.stackWidget.currentIndex())  # to adjust size font change

    def set_widgets_language(self, language):
        self.language = language
        number_of_main_widgets = self.stackWidget.count()
        for widget_number in range(number_of_main_widgets):
            widget = self.stackWidget.widget(widget_number)
            widget.set_language(language)
        self.menuBar().set_language(language)
        self.set_main_widget(self.stackWidget.currentIndex())  # to adjust size after language change


def main():
    app = QApplication([])
    app.setStyle("Fusion")
    window = InvestmentCalculator()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
