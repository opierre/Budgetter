from PySide2.QtWidgets import QGroupBox


class Card(QGroupBox):

    def __init__(self, parent):
        super().__init__(parent)

        ''' Set maximum height '''
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)

        ''' Card name '''
        self._name = ''

        ''' Card amount '''
        self._amount = 0

        ''' Card description '''
        self._description = ''

        ''' Layout '''
        self.layout = QH

    def setName(self, name):
        """
        Set Card name (title for GroupBox)
        :param name: card name
        :return: void
        """

        self._name = name
        self.setTitle(name)

    def getName(self):
        """
        Return card name
        :return: card name
        """

        return self._name

    def setAmount(self, amount):
        """
        Set card amount
        :param amount: card amount
        :return: void
        """

        self._amount = amount

    def getAmount(self):
        """
        Return card amount
        :return: card amount
        """

        return self._amount

    def setDescription(self, description):
        """
        Set card description
        :param description: card description
        :return: void
        """

        self._description = description

    def getDescription(self):
        """
        Return card description
        :return: card description
        """

        return self._description
