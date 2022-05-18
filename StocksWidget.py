from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QTableWidget, QLabel, QDoubleSpinBox, QTableWidgetItem


class StocksWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_widgets_and_text()
        self.init_and_set_layout()
        self.set_language()

    def init_widgets_and_text(self):
        self.risk_free_label_text = {"ENG": "Risk free interest", "PL": "Stopa wolna od ryzyka"}
        self.riskFreeInterestLabel = QLabel()

        self.riskFreeInterestInput = QDoubleSpinBox()
        self.riskFreeInterestInput.setValue(5)
        self.riskFreeInterestInput.setSuffix("%")
        self.riskFreeInterestInput.setDecimals(2)

        self.risk_premium_label_text = {"ENG": "Risk premium:", "PL": "Premia za ryzyko:"}
        self.riskPremiumLabel = QLabel()

        self.riskPremiumInput = QDoubleSpinBox()
        self.riskPremiumInput.setValue(3)
        self.riskPremiumInput.setSuffix("%")
        self.riskPremiumInput.setDecimals(2)

        self.betta_coefficient_label_text = {"ENG": "Beta coefficient:", "PL": "Współczynnik beta:"}
        self.bettaCoefficientLabel = QLabel()

        self.bettaCoefficientInput = QDoubleSpinBox()
        self.bettaCoefficientInput.setValue(1)
        self.bettaCoefficientInput.setDecimals(2)

        self.increase_coeficient_label_text = {"ENG": "Yearly Increase\n of dividend:", "PL": "Roczny wzrost\n dywidendy:"}
        self.increaseCoefficientLabel = QLabel()

        self.increaseCoefficientInput = QDoubleSpinBox()
        self.increaseCoefficientInput.setValue(1)
        self.increaseCoefficientInput.setSuffix("%")
        self.increaseCoefficientInput.setDecimals(2)

        self.tax_text = {"ENG": "Tax rate:", "PL": "Stopa podatkowa:"}
        self.taxLabel = QLabel()

        self.taxInput = QDoubleSpinBox()
        self.taxInput.setValue(19)
        self.taxInput.setMaximum(100)
        self.taxInput.setMinimum(0)
        self.taxInput.setSuffix("%")

        self.financial_label_text = {"ENG": "Financial date of company", "PL": "Dane finansowe przedsiębiorstwa"}
        self.financialHeaderLabel = QLabel()
        self.financialHeaderLabel.setAlignment(Qt.AlignHCenter)

        self.table_widget_text = {"ENG": (("Revenue", "Costs", "Amortization"),),
                                  "PL": (("Przychód", "Koszty", "Amortyzacja"),)}

        self.tableWidget = QTableWidget(10, 10)
        self.tableWidget.setMinimumSize(510, 200)

        self.net_present_value_label_text = {"ENG": "Net present value:", "PL": "Obecna wartość netto"}
        self.netPresentValueLabel = QLabel()

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
        layout.addWidget(self.netPresentValueLabel, 1, 2)
        layout.addWidget(self.netPresentValueLabelOutput, 1, 3)
        self.setLayout(layout)

    def set_language(self):
        self.riskFreeInterestLabel.setText(self.risk_free_label_text[self.parent().language])
        self.riskPremiumLabel.setText(self.risk_premium_label_text[self.parent().language])
        self.bettaCoefficientLabel.setText(self.betta_coefficient_label_text[self.parent().language])
        self.increaseCoefficientLabel.setText(self.increase_coeficient_label_text[self.parent().language])
        self.taxLabel.setText(self.tax_text[self.parent().language])
        self.financialHeaderLabel.setText(self.financial_label_text[self.parent().language])
        self.tableWidget.setItem(0, 0, QTableWidgetItem(self.table_widget_text[self.parent().language][0][0]))
        self.tableWidget.setItem(1, 0, QTableWidgetItem(self.table_widget_text[self.parent().language][0][1]))
        self.tableWidget.setItem(2, 0, QTableWidgetItem(self.table_widget_text[self.parent().language][0][2]))
        self.netPresentValueLabelOutput.setText(self.net_present_value_label_text[self.parent().language])

    def count_NPV(self):
        pass
