from PySide6.QtCore import QObject, Signal

from budgetter.utils.rest_client import RestClient
from budgetter.worker.worker import Worker


class Dashboard(QObject):
    """
    Dashboard panel services
    """

    # URLs List
    ACCOUNT_URL = "http://127.0.0.1:8080/api/budget/account/"

    # Signals list
    errorDashboard = Signal(tuple)
    accountAdded = Signal(object)

    def add_account_worker(self, name: str, amount: str, bank: str, date: str):
        """
        Add account via worker call

        :param name: account name
        :param amount: account amount
        :param bank: account bank
        :param date: date corresponding to account amount
        :return: None
        """

        # Build data
        data = {
            "name": name,
            "bank": 1,
            "amount": float(amount)
        }

        # Create worker
        worker = Worker(RestClient.post, url=self.ACCOUNT_URL, data=data)
        worker.signals.result.connect(self.accountAdded.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()
