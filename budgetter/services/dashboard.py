from PySide6.QtCore import QObject, Signal

from budgetter.utils.rest_client import RestClient
from budgetter.worker.worker import Worker


class Dashboard(QObject):
    """
    Dashboard panel services
    """

    # URLs List
    ACCOUNT_URL = "http://127.0.0.1:8080/api/budget/account/"
    BANK_URL = "http://127.0.0.1:8080/api/budget/bank/"

    # Signals list
    errorDashboard = Signal(tuple)
    accountAdded = Signal(object)
    bankAdded = Signal(object)
    banksFound = Signal(object)
    accountsFound = Signal(object)

    def get_banks_worker(self):
        """
        Retrieve all banks via worker call

        :return: None
        """

        # Create worker
        worker = Worker(RestClient.get, url=self.BANK_URL)
        worker.signals.result.connect(self.banksFound.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()

    def get_accounts_worker(self):
        """
        Retrieve all accounts via worker call

        :return: None
        """

        # Create worker
        worker = Worker(RestClient.get, url=self.ACCOUNT_URL)
        worker.signals.result.connect(self.accountsFound.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()

    def add_account_worker(self, name: str, amount: str, bank_id: int, date: str):
        """
        Add account via worker call

        :param name: account name
        :param amount: account amount
        :param bank_id: account bank identifier in database
        :param date: date for update
        :return: None
        """

        # Build data
        data = {
            "name": name,
            "bank": bank_id,
            "amount": float(amount.replace(',', '.')),
            "last_update": date
        }

        # Create worker
        worker = Worker(RestClient.post, url=self.ACCOUNT_URL, data=data)
        worker.signals.result.connect(self.accountAdded.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()

    def add_bank_worker(self, name: str):
        """
        Add bank via worker call

        :param name: account name
        :return: None
        """

        # Build data
        data = {
            "name": name
        }

        # Create worker
        worker = Worker(RestClient.post, url=self.BANK_URL, data=data)
        worker.signals.result.connect(self.bankAdded.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()