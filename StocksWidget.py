from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QTableWidget, QLabel, QDoubleSpinBox

from LanguageWidgets import LLabel


class StocksWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_widgets_and_text()
        self.init_and_set_layout()

    def init_widgets_and_text(self):
        self.riskFreeInterestLabel = LLabel()
        self.riskFreeInterestLabel.language_versions = {"ENG": "Risk free interest:",
                                                        "PL": "Stopa wolna od ryzyka:"}

        self.riskFreeInterestInput = QDoubleSpinBox()
        self.riskFreeInterestInput.setValue(5)
        self.riskFreeInterestInput.setSuffix("%")
        self.riskFreeInterestInput.setDecimals(2)

        self.riskPremiumLabel = LLabel()
        self.riskPremiumLabel.language_versions = {"ENG": "Risk premium:",
                                                   "PL": "Premia za ryzyko:"}

        self.riskPremiumInput = QDoubleSpinBox()
        self.riskPremiumInput.setValue(3)
        self.riskPremiumInput.setSuffix("%")
        self.riskPremiumInput.setDecimals(2)

        self.bettaCoefficientLabel = LLabel()
        self.bettaCoefficientLabel.language_versions = {"ENG": "Beta coefficient:",
                                                        "PL": "Współczynnik beta:"}

        self.bettaCoefficientInput = QDoubleSpinBox()
        self.bettaCoefficientInput.setValue(1)
        self.bettaCoefficientInput.setDecimals(2)

        self.increaseCoefficientLabel = LLabel()
        self.increaseCoefficientLabel.language_versions = {"ENG": "Yearly Increase\n of dividend:",
                                                           "PL": "Roczny wzrost\n dywidendy:"}

        self.increaseCoefficientInput = QDoubleSpinBox()
        self.increaseCoefficientInput.setValue(1)
        self.increaseCoefficientInput.setSuffix("%")
        self.increaseCoefficientInput.setDecimals(2)

        self.taxLabel = LLabel()
        self.taxLabel.language_versions = {"ENG": "Tax rate:",
                                           "PL": "Stopa podatkowa:"}

        self.taxInput = QDoubleSpinBox()
        self.taxInput.setValue(19)
        self.taxInput.setMaximum(100)
        self.taxInput.setMinimum(0)
        self.taxInput.setSuffix("%")

        self.financialHeaderLabel = LLabel()
        self.financialHeaderLabel.language_versions = {"ENG": "Financial date of company",
                                                       "PL": "Dane finansowe przedsiębiorstwa"}
        self.financialHeaderLabel.setAlignment(Qt.AlignHCenter)

        self.table_widget_text = {"ENG": (("Revenue", "Costs", "Amortization"),),
                                  "PL": (("Przychód", "Koszty", "Amortyzacja"),)}

        self.tableWidget = QTableWidget(30, 30)
        self.tableWidget.setMinimumSize(510, 200)

        self.netPresentValueLabel = LLabel()
        self.netPresentValueLabel.language_versions = {"ENG": "Net present value:",
                                                       "PL": "Obecna wartość netto:"}

        self.netPresentValueLabelOutput = QLabel()

    def init_and_set_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.riskFreeInterestLabel, 1, 0)
        layout.addWidget(self.riskFreeInterestInput, 2, 0)
        layout.addWidget(self.riskPremiumLabel, 3, 0)
        layout.addWidget(self.riskPremiumInput, 4, 0)
        layout.addWidget(self.bettaCoefficientLabel, 5, 0)
        layout.addWidget(self.bettaCoefficientInput, 6, 0)
        layout.addWidget(self.increaseCoefficientLabel, 7, 0)
        layout.addWidget(self.increaseCoefficientInput, 8, 0)
        layout.addWidget(self.taxLabel, 1, 1)
        layout.addWidget(self.taxInput, 2, 1)
        layout.addWidget(self.financialHeaderLabel, 0, 2)
        layout.addWidget(self.tableWidget, 1, 2, 8, 1)
        layout.addWidget(self.netPresentValueLabel, 1, 3)
        layout.addWidget(self.netPresentValueLabelOutput, 2, 3)
        layout.setHorizontalSpacing(15)
        self.setLayout(layout)

    def set_language(self, language):
        for child in self.children():
            try:
                child.set_language(language)
            except AttributeError:
                continue

    def count_NPV(self):
        pass
