import datetime

from PySide6.QtCore import QObject, Signal, QThreadPool


from budgetter.worker.rest_client import RestClient
from budgetter.worker.worker import Worker


class Dashboard(QObject):
    """
    Dashboard panel services
    """

    # URLs List
    ACCOUNT_URL = "http://127.0.0.1:9090/api/budget/account/"
    BANK_URL = "http://127.0.0.1:9090/api/budget/bank/"
    TRANSACTION_URL = "http://127.0.0.1:9090/api/budget/transaction/"
    OFX_URL = "http://127.0.0.1:9090/api/budget/ofx/upload-ofx/"
    EXPENSES_URL = "http://127.0.0.1:9090/api/budget/expenses/"
    EXPENSES_DISTRIBUTION_URL = f"{EXPENSES_URL}distribution/"

    # Signals list
    errorDashboard = Signal(tuple)
    accountAdded = Signal(object)
    bankAdded = Signal(object)
    banksFound = Signal(object)
    accountsFound = Signal(object)
    transactionAdded = Signal(object)
    transactionRemoved = Signal(object)
    transactionEdited = Signal(object)
    transactionsFound = Signal(object)
    expensesDistribution = Signal(object)
    transactionsPosted = Signal(object)

    def __init__(self):
        super().__init__()

        # Retrieve current thread pool to start worker threads
        self._thread_pool = QThreadPool.globalInstance()

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
        self._thread_pool.start(worker)

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
        self._thread_pool.start(worker)

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
        self._thread_pool.start(worker)

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
        self._thread_pool.start(worker)

    def add_account_worker(
            self, name: str, number: str, amount: str, bank_id: int, date: str, color: str
    ):
        """
        Add account via worker call

        :param name: account name
        :param number: account number
        :param amount: account amount
        :param bank_id: account bank identifier in database
        :param date: date for update
        :param color: color for account
        :return: None
        """

        # Build data
        data = {
            "name": name,
            "account_id": number,
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
        self._thread_pool.start(worker)

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
        self._thread_pool.start(worker)

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

        # Create worker
        worker = Worker(RestClient.post, url=self.TRANSACTION_URL, data=data)
        worker.signals.result.connect(self.transactionAdded.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        self._thread_pool.start(worker)

    def remove_transaction_worker(self, transaction_id: int):
        """
        Delete transaction from database

        :param transaction_id: transaction ID to remove
        :return: None
        """

        # Create worker
        worker = Worker(
            RestClient.delete, url=f"{self.TRANSACTION_URL}{transaction_id}/"
        )
        worker.signals.result.connect(self.transactionRemoved.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        self._thread_pool.start(worker)

    def import_ofx(self, ofx_path: str):
        """
        Import OFX file with transactions for parsing

        :param ofx_path: ofx file path
        :return:
        """

        # Create worker
        worker = Worker(
            RestClient.post, url=f"{self.OFX_URL}", file_path=ofx_path
        )
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        self._thread_pool.start(worker)

    def edit_transaction_worker(
            self,
            transaction_type: str,
            category: str,
            name: str,
            amount: str,
            amount_date: str,
            mean: str,
            notes: str,
            account_id: int,
            transaction_id: int,
    ):
        """
        Edit transaction via worker call

        :param transaction_type: transaction type (income, expenses, transfer)
        :param category: category
        :param name: account name
        :param amount: account amount
        :param amount_date: account amount in date
        :param mean: transaction mean
        :param notes: notes
        :param account_id: account ID
        :param transaction_id: transaction ID
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

        # Create worker
        worker = Worker(
            RestClient.patch, url=f"{self.TRANSACTION_URL}{transaction_id}/", data=data
        )
        worker.signals.result.connect(self.transactionEdited.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        self._thread_pool.start(worker)

    def add_transactions(self, data: dict):
        """
        Push transactions to database

        :param data: data with transactions
        :return: None
        """

        # Create worker
        worker = Worker(RestClient.post, url=self.TRANSACTION_URL, data=data.get("transactions"))
        worker.signals.result.connect(self.transactionsPosted.emit)
        worker.signals.error.connect(self.errorDashboard.emit)

        # Start worker
        self._thread_pool.start(worker)
