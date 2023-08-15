import datetime

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
    TRANSACTION_URL = "http://127.0.0.1:8080/api/budget/transaction/"
    EXPENSES_URL = "http://127.0.0.1:8080/api/budget/expenses/"
    EXPENSES_DISTRIBUTION_URL = f"{EXPENSES_URL}distribution/"

    # Signals list
    errorDashboard = Signal(tuple)
    accountAdded = Signal(object)
    bankAdded = Signal(object)
    banksFound = Signal(object)
    accountsFound = Signal(object)
    transactionAdded = Signal(object)
    transactionsFound = Signal(object)
    expensesDistribution = Signal(object)

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

    def get_transactions_worker(self):
        """
        Retrieve all transactions via worker call

        :return: None
        """

        # Create worker
        worker = Worker(RestClient.get, url=self.TRANSACTION_URL)
        worker.signals.result.connect(self.transactionsFound.emit)
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

    def get_expenses_distribution_worker(self):
        """
        Retrieve expenses distribution via worker call

        :return: None
        """

        # Create worker
        worker = Worker(RestClient.get, url=self.EXPENSES_DISTRIBUTION_URL)
        worker.signals.result.connect(self.expensesDistribution.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()

    def add_account_worker(
            self, name: str, amount: str, bank_id: int, date: str, color: str
    ):
        """
        Add account via worker call

        :param name: account name
        :param amount: account amount
        :param bank_id: account bank identifier in database
        :param date: date for update
        :param color: color for account
        :return: None
        """

        # Build data
        data = {
            "name": name,
            "bank": bank_id,
            "amount": float(amount.replace(",", ".")),
            "last_update": date,
            "color": color,
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
        data = {"name": name}

        # Create worker
        worker = Worker(RestClient.post, url=self.BANK_URL, data=data)
        worker.signals.result.connect(self.bankAdded.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()

    def add_transaction_worker(
            self,
            transaction_type: str,
            category: str,
            name: str,
            amount: str,
            amount_date: str,
            mean: str,
            notes: str,
            account_id: int,
    ):
        """
        Add transaction via worker call

        :param transaction_type: transaction type (income, expenses, transfer)
        :param category: category
        :param name: account name
        :param amount: account amount
        :param amount_date: account amount in date
        :param mean: transaction mean
        :param notes: notes
        :param account_id: account ID
        :return: None
        """

        # Build data
        data = {
            "name": name,
            "amount": amount,
            "date": datetime.datetime.strptime(amount_date, "%d/%m/%Y").strftime(
                "%Y-%m-%d"
            ),
            "account": account_id,
            "category": category if category else None,
            "comment": notes,
            "mean": mean.upper(),
            "transaction_type": transaction_type.upper(),
        }

        print(data)

        # Create worker
        worker = Worker(RestClient.post, url=self.TRANSACTION_URL, data=data)
        worker.signals.result.connect(self.transactionAdded.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        worker.run()
