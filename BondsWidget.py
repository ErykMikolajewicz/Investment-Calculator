from datetime import date

from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QDoubleSpinBox, QDateEdit

from LanguageWidgets import LLabel, LComboBox, LErrorMessage


class BondsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_numerical_fields()
        self.init_widgets_and_text()
        self.init_and_set_layout()
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
        self.nominalBondValueLabel = LLabel()
        self.nominalBondValueLabel.language_versions = {"ENG": "Nominal bond value:",
                                                        "PL": "Wartość nominalna obligacji:"}
        self.nominalBondValueInput = QDoubleSpinBox()
        self.nominalBondValueInput.setMaximum(10 ** 9)
        self.nominalBondValueInput.setMinimum(0)
        self.nominalBondValueInput.setValue(1000)
        self.nominalBondValueInput.valueChanged.connect(self.count_and_set_values)

        self.interestRateLabel = LLabel()
        self.interestRateLabel.language_versions = {"ENG": "Interest rate:",
                                                    "PL": "Oprocentowanie:"}
        self.interestRateInput = QDoubleSpinBox()
        self.interestRateInput.setValue(2)
        self.interestRateInput.setMaximum(600)
        self.interestRateInput.setSuffix("%")
        self.interestRateInput.valueChanged.connect(self.count_and_set_values)

        self.bondPurchaseValueLabel = LLabel()
        self.bondPurchaseValueLabel.language_versions = {"ENG": "Bond purchase value:",
                                                         "PL": "Cena kupna obligacji:"}
        self.bondPurchaseValueInput = QDoubleSpinBox()
        self.bondPurchaseValueInput.setMaximum(10 ** 9)
        self.bondPurchaseValueInput.setMinimum(0.01)
        self.bondPurchaseValueInput.setValue(1000)
        self.bondPurchaseValueInput.valueChanged.connect(self.count_and_set_values)

        self.currentDateLabel = LLabel()
        self.currentDateLabel.language_versions = {"ENG": "Current date:",
                                                   "PL": "Obecna data:"}
        self.purchaseDate = QDateEdit(date.today())
        self.purchaseDate.dateChanged.connect(self.count_and_set_values)

        self.redemptionDateLabel = LLabel()
        self.redemptionDateLabel.language_versions = {"ENG": "Redemption date:",
                                                      "PL": "Data wykupu:"}
        redemption_date = self.purchaseDate.date().addYears(10)
        self.redemptionDate = QDateEdit(redemption_date)
        self.redemptionDate.dateChanged.connect(self.count_and_set_values)

        self.capitalizationPeriodLabel = LLabel()
        self.capitalizationPeriodLabel.language_versions = {"ENG": "Capitalization period:",
                                                            "PL": "Okres kapitalizacji:"}

        self.capitalizationPeriodChoose = LComboBox()
        self.capitalizationPeriodChoose.language_versions = {"ENG": ('yearly', 'half-yearly',
                                                                     'quarterly', 'monthly'),
                                                             "PL": ('rocznie', 'półrocznie',
                                                                    'kwartalnie', 'miesięcznie')}
        self.capitalizationPeriodChoose.currentIndexChanged.connect(self.count_and_set_values)

        self.simpleYieldLabel = LLabel()
        self.simpleYieldLabel.language_versions = {"ENG": "Simple yield:",
                                                   "PL": "Prosta stopa zwrotu:"}
        self.simpleYieldOutputLabel = QLabel()

        self.ytmBruttoLabel = QLabel("ytm brutto:")
        self.ytmBruttoOutputLabel = QLabel()

        self.ytmNettoLabel = QLabel("ytm netto:")
        self.ytmNettoOutputLabel = QLabel()

        self.durationLabel = QLabel("Duration:")
        self.durationOutputLabel = QLabel()

        self.interestRateChangeLabel = LLabel()
        self.interestRateChangeLabel.language_versions = {"ENG": "Interest rate change:",
                                                          "PL": "Zmiana stopy procentowej:"}
        self.interestRateChangeInput = QDoubleSpinBox()
        self.interestRateChangeInput.setMaximum(600)
        self.interestRateChangeInput.setMinimum(-600)
        self.interestRateChangeInput.setValue(1)
        self.interestRateChangeInput.setSuffix("%")
        self.interestRateChangeInput.valueChanged.connect(self.count_impact_of_interest_rate_change)

        self.impactInterestRateLabel = LLabel()
        self.impactInterestRateLabel.language_versions = {"ENG": "Impact for bond value:",
                                                          "PL": "Wpływ na cenę obligacji:"}
        self.impactInterestRateOutputLabel = QLabel()

        self.badDatePopup = LErrorMessage()
        self.badDatePopup.language_versions = {"ENG": "Bad date range!",
                                               "PL": "Niepoprawny zakre dat!"}

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
        layout.setHorizontalSpacing(15)
        self.setLayout(layout)

    def set_language(self, language):
        for child in self.children():
            try:
                child.set_language(language)
            except AttributeError:
                continue

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
        bond_value_by_higher_interest = self.count_bond_value_by_ytm(self.ytm + self.interestRateChangeInput.value())
        price_change = bond_value_by_higher_interest/self.bondPurchaseValueInput.value() - 1
        price_change = round(price_change*100, 2)
        self.impactInterestRateOutputLabel.setText(str(price_change) + "%")
