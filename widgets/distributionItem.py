from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy


class DistributionItem(QWidget):
    """
    Distribution Item with icon, category, number of transactions,
    total amount, percentage
    """

    def __init__(self):
        super().__init__()

        """ Store Grid Layout """
        self.layout = QGridLayout(self)

        """ Store category icon """
        self.icon = QPushButton("")

        """ Store category """
        self.category = QLabel("Restaurants")

        """ Store number of transactions """
        self.nbTransactions = QLabel("3 transactions")

        """ Store total amount """
        self.amount = QLabel("€ 192")

        """ Store percentage """
        self.percentage = QLabel("32%")

        """ Store spacers """
        self.spacerRow1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacerRow2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        """ Configure Layout """
        self.configureLayout()

    def configureLayout(self):
        """
        Configure layout and add widgets
        :return: void
        """

        """ Set margins """
        self.layout.setContentsMargins(0, 0, 0, 0)

        """ Add icon, span over two rows """
        self.layout.addWidget(self.icon, 0, 0, 1, 0)

        """ Add category """
        self.layout.addWidget(self.category, 0, 1, 0, 0)

        """ Add number of transactions """
        self.layout.addWidget(self.nbTransactions, 1, 0, 0, 0)

        """ Add spacers """
        self.layout.addItem(self.spacerRow1, 0, 2, 0, 0)
        self.layout.addItem(self.spacerRow2, 1, 2, 0, 0)

        """ Add amount """
        self.layout.addWidget(self.amount, 0, 3, 0, 0)

        """ Add percentage """
        self.layout.addWidget(self.percentage, 1, 3, 0, 0)

    def setValue(self, value):
        """
        Update all widgets displayed
        :param value: [category to set, number of transactions to set,
        total amount for this category, percentage]
        :return: void
        """

        self.category.setText(value[0])
        self.nbTransactions.setText(value[1])
        self.amount.setText(str(int(value[2])))
        self.percentage.setText(value[3])

    def value(self):
        """
        Return list with all values
        :return: all values in a list
        """

        return [self.category.text(), self.nbTransactions.text(),
                self.amount.text(), self.percentage.text()]

    def category(self):
        """
        Getter for category
        :return: category
        """

        return self.category.text()

    def transactions(self):
        """
        Getter for number of transactions
        :return: number of transactions
        """

        return self.nbTransactions.text()

    def amount(self):
        """
        Getter for total amount
        :return: amount
        """

        return self.amount.text()

    def percentage(self):
        """
        Getter for percentage
        :return: percentage
        """

        return self.percentage.text()
