from PySide6.QtWidgets import (QWidget,
                               QGridLayout,
                               QLabel,
                               QDoubleSpinBox,
                               QDateEdit,
                               QComboBox,
                               QErrorMessage)
from datetime import date


class BondsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_numerical_fields()
        self.init_widgets_and_text()
        self.init_and_set_layout()
        self.set_language()
        self.count_and_set_values()

    def init_numerical_fields(self):
        self.simple_yield = 0
        self.capitalization_periods_in_year = 1
        self.capitalization_period = (0, 0)
        self.ytm = 0
        self.ytm_netto = 0
        self.duration = 0
        self.saving_options = (12, 6, 3, 1)

    def init_widgets_and_text(self):
        self.nominal_bond_value_text = {"ENG": "Nominal bond value:", "PL": "Wartość nominalna obligacji:"}
        self.nominalBondValueLabel = QLabel()
        self.nominalBondValueInput = QDoubleSpinBox()
        self.nominalBondValueInput.setMaximum(10 ** 9)
        self.nominalBondValueInput.setMinimum(0)
        self.nominalBondValueInput.setValue(1000)
        self.nominalBondValueInput.valueChanged.connect(self.count_and_set_values)

        self.interest_rate_text = {"ENG": "Interest rate:", "PL": "Oprocentowanie:"}
        self.interestRateLabel = QLabel()
        self.interestRateInput = QDoubleSpinBox()
        self.interestRateInput.setValue(2)
        self.interestRateInput.setMaximum(600)
        self.interestRateInput.setSuffix("%")
        self.interestRateInput.valueChanged.connect(self.count_and_set_values)

        self.bond_purchase_value_text = {"ENG": "Bond purchase value:", "PL": "Cena kupna obligacji:"}
        self.bondPurchaseValueLabel = QLabel()
        self.bondPurchaseValueInput = QDoubleSpinBox()
        self.bondPurchaseValueInput.setMaximum(10 ** 9)
        self.bondPurchaseValueInput.setMinimum(0.01)
        self.bondPurchaseValueInput.setValue(1000)
        self.bondPurchaseValueInput.valueChanged.connect(self.count_and_set_values)

        self.current_date_text = {"ENG": "Current date:", "PL": "Obecna data:"}
        self.currentDateLabel = QLabel()
        self.purchaseDate = QDateEdit(date.today())
        self.purchaseDate.dateChanged.connect(self.count_and_set_values)

        self.redemption_date_text = {"ENG": "Redemption date:", "PL": "Data wykupu:"}
        self.redemptionDateLabel = QLabel()
        redemption_date = self.purchaseDate.date().addYears(10)
        self.redemptionDate = QDateEdit(redemption_date)
        self.redemptionDate.dateChanged.connect(self.count_and_set_values)

        self.capitalization_period_text = {"ENG": "capitalization period:", "PL": "Okres kapitalizacji:"}
        self.capitalizationPeriodLabel = QLabel()
        self.capitalization_period_choose_text = {"ENG": ('yearly', 'half-yearly', 'quarterly', 'monthly'),
                                                  "PL": ('rocznie', 'półrocznie', 'kwartalnie', 'miesięcznie')}
        self.capitalizationPeriodChoose = QComboBox()
        self.capitalizationPeriodChoose.currentIndexChanged.connect(self.count_and_set_values)

        self.simple_yield_text = {"ENG": "Simple yield:", "PL": "Prosta stopa zwrotu:"}
        self.simpleYieldLabel = QLabel()
        self.simpleYieldOutputLabel = QLabel()

        self.ytmBruttoLabel = QLabel("ytm brutto:")
        self.ytmBruttoOutputLabel = QLabel()

        self.ytmNettoLabel = QLabel("ytm netto:")
        self.ytmNettoOutputLabel = QLabel()

        self.durationLabel = QLabel("Duration:")
        self.durationOutputLabel = QLabel()

        self.interest_rate_change_text = {"ENG": "Interest rate change:", "PL": "Zmiana stopy procentowej:"}
        self.interestRateChangeLabel = QLabel()
        self.interestRateChangeInput = QDoubleSpinBox()
        self.interestRateChangeInput.setMaximum(600)
        self.interestRateChangeInput.setMinimum(-600)
        self.interestRateChangeInput.setValue(1)
        self.interestRateChangeInput.setSuffix("%")
        self.interestRateChangeInput.valueChanged.connect(self.count_impact_of_interest_rate_change)

        self.impact_interest_rate_text = {"ENG": "Impact for bond value:",
                                          "PL": "Wpływ na cenę obligacji:"}
        self.impactInterestRateLabel = QLabel()
        self.impactInterestRateOutputLabel = QLabel()

        self.bad_date_popup_text = {"ENG": "Bad date range!",
                                    "PL": "Niepoprawny zakre dat!"}
        self.badDatePopup = QErrorMessage(self)

    def init_and_set_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.nominalBondValueLabel, 0, 0)
        layout.addWidget(self.nominalBondValueInput, 1, 0)
        layout.addWidget(self.interestRateLabel, 2, 0)
        layout.addWidget(self.interestRateInput, 3, 0)
        layout.addWidget(self.bondPurchaseValueLabel, 4, 0)
        layout.addWidget(self.bondPurchaseValueInput, 5, 0)
        layout.addWidget(self.currentDateLabel, 0, 1)
        layout.addWidget(self.purchaseDate, 1, 1)
        layout.addWidget(self.redemptionDateLabel, 2, 1)
        layout.addWidget(self.redemptionDate, 3, 1)
        layout.addWidget(self.capitalizationPeriodLabel, 4, 1)
        layout.addWidget(self.capitalizationPeriodChoose, 5, 1)
        layout.addWidget(self.simpleYieldLabel, 0, 2)
        layout.addWidget(self.simpleYieldOutputLabel, 1, 2)
        layout.addWidget(self.ytmBruttoLabel, 2, 2)
        layout.addWidget(self.ytmBruttoOutputLabel, 3, 2)
        layout.addWidget(self.ytmNettoLabel, 4, 2)
        layout.addWidget(self.ytmNettoOutputLabel, 5, 2)
        layout.addWidget(self.durationLabel, 0, 3)
        layout.addWidget(self.durationOutputLabel, 1, 3)
        layout.addWidget(self.interestRateChangeLabel, 2, 3)
        layout.addWidget(self.interestRateChangeInput, 3, 3)
        layout.addWidget(self.impactInterestRateLabel, 4, 3)
        layout.addWidget(self.impactInterestRateOutputLabel, 5, 3)
        self.setLayout(layout)

    def set_language(self):
        self.nominalBondValueLabel.setText(self.nominal_bond_value_text[self.parent().language])
        self.interestRateLabel.setText(self.interest_rate_text[self.parent().language])
        self.bondPurchaseValueLabel.setText(self.bond_purchase_value_text[self.parent().language])
        self.currentDateLabel.setText(self.current_date_text[self.parent().language])
        self.redemptionDateLabel.setText(self.redemption_date_text[self.parent().language])
        self.capitalizationPeriodLabel.setText(self.capitalization_period_text[self.parent().language])
        self.capitalizationPeriodChoose.clear()
        self.capitalizationPeriodChoose.addItems(self.capitalization_period_choose_text[self.parent().language])
        self.simpleYieldLabel.setText(self.simple_yield_text[self.parent().language])
        self.interestRateChangeLabel.setText(self.interest_rate_change_text[self.parent().language])
        self.impactInterestRateLabel.setText(self.impact_interest_rate_text[self.parent().language])

    def count_and_set_values(self):
        self.count_simple_yield()
        self.count_capitalization_period()
        self.count_ytm()
        self.count_duration()
        self.simpleYieldOutputLabel.setText(self.simple_yield)
        self.ytmBruttoOutputLabel.setText(str(self.ytm) + "%")
        self.ytmNettoOutputLabel.setText(str(self.ytm_netto) + "%")
        self.durationOutputLabel.setText(str(self.duration))
        self.count_impact_of_interest_rate_change()  # also sets a value because is used independently

    def count_simple_yield(self):
        bond_interest = self.interestRateInput.value() * self.nominalBondValueInput.value()
        simple_yield = bond_interest/ self.bondPurchaseValueInput.value()
        simple_yield = round(simple_yield, 2)
        self.simple_yield = str(simple_yield) + "%"

    def count_capitalization_period(self):
        start_date = self.purchaseDate.date()
        end_date = self.redemptionDate.date()
        saving_option = self.capitalizationPeriodChoose.currentIndex()
        self.capitalization_periods_in_year = 12 / self.saving_options[saving_option]
        months_to_next_capitalization = self.saving_options[saving_option]
        number_of_full_capitalization_period = 0
        while start_date.addMonths(months_to_next_capitalization) < end_date:
            start_date = start_date.addMonths(months_to_next_capitalization)
            number_of_full_capitalization_period += 1
        not_full_period = (start_date.daysTo(end_date) - 1)/start_date.daysInYear() * self.capitalization_periods_in_year
        self.capitalization_period = (number_of_full_capitalization_period, not_full_period)

    def count_ytm(self):
        if self.redemptionDate.date() <= self.purchaseDate.date():
            self.badDatePopup.showMessage(self.bad_date_popup_text[self.parent().language])
            return
        self.ytm = 0
        computing_steps = [1, 0.1, 0.01, 0.001]
        for step in computing_steps:
            while True:
                bond_value_by_ytm = self.count_bond_value_by_ytm(self.ytm)
                if bond_value_by_ytm < self.bondPurchaseValueInput.value():
                    self.ytm -= step
                    break
                self.ytm += step
        self.ytm_netto = round(self.ytm*0.81, 2)
        self.ytm = round(self.ytm, 2)

    def count_bond_value_by_ytm(self, ytm):
        yearly_interest = self.nominalBondValueInput.value() * self.interestRateInput.value()/100
        period_interest = yearly_interest/self.capitalization_periods_in_year
        discounted_interest = 0
        discount_factor = 1 + ytm/100/self.capitalization_periods_in_year
        for number_full_period in range(self.capitalization_period[0] + 1):
            discounted_interest += period_interest/discount_factor**(number_full_period + self.capitalization_period[1])
        discounted_bond_price = self.nominalBondValueInput.value()/discount_factor**sum(self.capitalization_period)
        bond_value = discounted_bond_price + discounted_interest
        return bond_value

    def count_duration(self):
        yearly_interest = self.nominalBondValueInput.value() * self.interestRateInput.value() / 100
        period_interest = yearly_interest/self.capitalization_periods_in_year
        discount_factor = 1 + self.ytm/100/self.capitalization_periods_in_year
        duration_sum = 0
        for number_full_period in range(self.capitalization_period[0] + 1):
            duration_sum += (number_full_period + self.capitalization_period[1])/\
                            self.capitalization_periods_in_year * period_interest/discount_factor\
                            **(number_full_period + self.capitalization_period[1])
        duration_sum += sum(self.capitalization_period)/self.capitalization_periods_in_year\
                        *self.nominalBondValueInput.value()/\
                        discount_factor**sum(self.capitalization_period)
        self.duration = duration_sum / self.bondPurchaseValueInput.value()
        self.duration = round(self.duration, 2)

    def count_impact_of_interest_rate_change(self):
        value_percent_change = -self.duration/(1 + self.ytm/100)*self.interestRateChangeInput.value()
        value_percent_change = round(value_percent_change, 2)
        self.impactInterestRateOutputLabel.setText(str(value_percent_change) + "%")
