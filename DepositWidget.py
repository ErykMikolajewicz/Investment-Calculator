from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget,
                               QGridLayout,
                               QDateEdit,
                               QDoubleSpinBox,
                               QLabel,
                               QComboBox,
                               QPushButton,
                               QErrorMessage)
from datetime import date


class DepositWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.yield_ = ""
        self.init_widgets_and_text()
        self.init_and_set_layout()
        self.set_language()

    def init_widgets_and_text(self):
        self.capitalLabelText = {"ENG": "Deposit amount:", "PL": "Kwota lokaty:"}
        self.capitalLabel = QLabel()

        self.interestRateLabelText = {"ENG": "Interest rate:", "PL": "Oprocentowanie:"}
        self.interestRateLabel = QLabel()

        self.capitalizationPeriodLabelText = {"ENG": "Period of capitalization:", "PL": "Okres kapitalizacji:"}
        self.capitalizationPeriodLabel = QLabel()

        self.savingPeriodLabelText = {"ENG": "Saving period:", "PL": "Czas oszczędzania:"}
        self.savingPeriodLabel = QLabel()

        self.startTimeLabelText = {"ENG": "for:", "PL": "od:"}
        self.startTimeLabel = QLabel()

        self.endTimeLabelText = {"ENG": "to:", "PL": "do:"}
        self.endTimeLabel = QLabel()

        self.yieldLabelText = {"ENG": "Yield: ", "PL": "Zysk: "}
        self.yieldLabel = QLabel()

        self.capitalInput = QDoubleSpinBox()
        self.capitalInput.setMaximum(10 ** 9)
        self.capitalInput.setValue(1000)

        self.interestRateInput = QDoubleSpinBox()
        self.interestRateInput.setMaximum(600)
        self.interestRateInput.setValue(2)
        self.interestRateInput.setSuffix("%")

        self.saving_period_start = QDateEdit(date.today())
        self.saving_period_end = QDateEdit(date.today())

        self.capitalizationPeriodChooseText = {"ENG": ('every day', 'on end of moth', 'year', 'on end of period'),
                                               "PL": ('codziennie', 'na koniec miesiąca', 'rok', 'na koniec okresu')}
        self.capitalizationPeriodChoose = QComboBox()

        self.countButtonText = {"ENG": "Count yield!", "PL": "Policz zysk!"}
        self.countButton = QPushButton()
        self.countButton.clicked.connect(self.count_yield)

        self.tax_text = {"ENG" : "Tax rate:", "PL" : "Stopa podatkowa:"}
        self.taxLabel = QLabel()

        self.taxInput = QDoubleSpinBox()
        self.taxInput.setValue(19)
        self.taxInput.setMaximum(100)
        self.taxInput.setMinimum(0)
        self.taxInput.setSuffix("%")

        self.payed_tax_text = {"ENG" : "Payed tax:", "PL" : "Zapłacony podatek:"}
        self.payedTaxLabel = QLabel()

        self.payedTaxOutputLabel = QLabel()

        self.bad_date_popup_text = {"ENG": "Bad date range!",
                                    "PL": "Niepoprawny zakre dat!"}
        self.badDatePopup = QErrorMessage(self)

    def init_and_set_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.capitalLabel, 0, 0)
        layout.addWidget(self.capitalInput, 1, 0)
        layout.addWidget(self.interestRateLabel, 2, 0)
        layout.addWidget(self.interestRateInput, 3, 0)
        layout.addWidget(self.savingPeriodLabel, 0, 1, 1, 4, Qt.AlignVCenter | Qt.AlignHCenter)
        layout.addWidget(self.startTimeLabel, 1, 1, Qt.AlignRight)
        layout.addWidget(self.saving_period_start, 1, 2, Qt.AlignLeft)
        layout.addWidget(self.endTimeLabel, 1, 3, Qt.AlignRight)
        layout.addWidget(self.saving_period_end, 1, 4, Qt.AlignLeft)
        layout.addWidget(self.capitalizationPeriodLabel, 2, 1, 1, 2)
        layout.addWidget(self.capitalizationPeriodChoose, 3, 1, 1, 2)
        layout.addWidget(self.countButton, 2, 3, 1, 2)
        layout.addWidget(self.yieldLabel, 3, 3, 1, 2)
        layout.addWidget(self.taxLabel, 0, 5)
        layout.addWidget(self.taxInput, 1, 5)
        layout.addWidget(self.payedTaxLabel, 2, 5)
        layout.addWidget(self.payedTaxOutputLabel, 3, 5)
        self.setLayout(layout)

    def set_language(self):
        self.capitalLabel.setText(self.capitalLabelText[self.parent().language])
        self.interestRateLabel.setText(self.interestRateLabelText[self.parent().language])
        self.capitalizationPeriodLabel.setText(self.capitalizationPeriodLabelText[self.parent().language])
        self.startTimeLabel.setText(self.startTimeLabelText[self.parent().language])
        self.endTimeLabel.setText(self.endTimeLabelText[self.parent().language])
        self.savingPeriodLabel.setText(self.savingPeriodLabelText[self.parent().language])
        self.capitalizationPeriodChoose.clear()
        self.capitalizationPeriodChoose.addItems(self.capitalizationPeriodChooseText[self.parent().language])
        self.countButton.setText(self.countButtonText[self.parent().language])
        self.yieldLabel.setText(self.yieldLabelText[self.parent().language])
        self.taxLabel.setText(self.tax_text[self.parent().language])
        self.payedTaxLabel.setText(self.payed_tax_text[self.parent().language])

    def count_yield(self):
        self.yield_ = ''
        start_date = self.saving_period_start.date()
        end_date = self.saving_period_end.date()
        if start_date >= end_date:
            self.badDatePopup.showMessage(self.bad_date_popup_text[self.parent().language])
            return

        capital = self.capitalInput.value()
        interest_rate = self.interestRateInput.value()/100
        saving_option = self.capitalizationPeriodChoose.currentIndex()
        variants_saving_list = [lambda: 1,
                                lambda: start_date.daysInMonth() + 1 - start_date.day(),
                                lambda: start_date.daysTo(start_date.addYears(1)),
                                lambda: start_date.daysTo(end_date)]
        def round_up(number, decimals = 2):
            decimals = 10**-decimals
            answer = number // decimals
            if (number/decimals) == answer: # to don't round up 100.01 to 100.02 for example
                return answer*decimals
            answer = answer * decimals + decimals
            return answer
        payed_tax = 0
        while start_date < end_date:
            interest_rate_days = variants_saving_list[saving_option]()
            start_date = start_date.addDays(interest_rate_days)
            if start_date > end_date:
                break
            saving_time_in_year = interest_rate_days/start_date.daysInYear()
            interest = capital*interest_rate*saving_time_in_year
            interest = round(interest, 2)
            if interest > 0:
                tax = round_up(interest*self.taxInput.value()/100, 2)
                payed_tax += tax
                interest -= tax
            capital += interest
        self.yield_ = str(round(capital - self.capitalInput.value(), 2))
        self.yieldLabel.setText(self.yieldLabelText[self.parent().language] + str(self.yield_))
        self.payedTaxOutputLabel.setText(str(payed_tax))
