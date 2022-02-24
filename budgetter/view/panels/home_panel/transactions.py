from PySide2.QtCore import QObject, Qt, QDate, QRect, QSize, QItemSelectionModel, QCoreApplication
from PySide2.QtGui import QIcon, QFont, QFontMetrics
from PySide2.QtWidgets import QVBoxLayout, QStatusBar, QWidget, QPushButton, QListView, QFrame, QLineEdit, \
    QDoubleSpinBox, QDateEdit, QComboBox, QLabel, QAbstractItemView

from budgetter.models.transactions_model import TransactionsModel, TransactionsFilterModel
from budgetter.view.widgets.transaction_widgets.calendar_widget import CalendarWidget
from budgetter.view.widgets.transaction_widgets.category_combobox_delegate import CategoryComboBox
from budgetter.view.widgets.transaction_widgets.expense_income_transfer_widget import ExpensesIncomeTransfer
from budgetter.view.widgets.status_bar import StatusBar
from budgetter.view.widgets.transaction_widgets.means_widget import Mean
from budgetter.view.widgets.transaction_widgets.transaction_delegate import TransactionDelegate


class Transactions(QObject):
    """
    Transactions
    """

    def __init__(self, gui, parent):
        super().__init__()

        # Store gui and main window
        self.ui_setup = gui
        self.main_window = parent

        # Store custom/classic status bar
        self.custom_status_bar = StatusBar()
        self.status_bar = QStatusBar()

        # All button - Type
        self.all = QPushButton(QCoreApplication.translate("transactions", "All"))

        # Expenses button - Type
        self.expenses = QPushButton(QCoreApplication.translate("transactions", "Expenses"))

        # Incomes button - Type
        self.income = QPushButton(QCoreApplication.translate("transactions", "Income"))

        # Transfers button - Type
        self.transfer = QPushButton(QCoreApplication.translate("transactions", "Transfer"))

        # All button - Account
        self.all_account = QPushButton(QCoreApplication.translate("transactions", "All"))

        # Account 1 button - Account
        self.account1 = QPushButton("Livret A")

        # Account 2 button - Account
        self.account2 = QPushButton("Compte Chèque")

        # Account 3 button - Account
        self.account3 = QPushButton("Livret Jeune")

        # Store item delegate
        self.transaction_delegate = TransactionDelegate()

        # ListView to display all transactions
        self.transactions_listview = QListView()

        # Store LineEdit for name edition on transaction
        self.edit_name = QLineEdit(self.transactions_listview)

        # Store Combobox for category selection on transaction
        self.edit_category = QComboBox(self.transactions_listview)
        self.edit_category_name = QLabel(self.transactions_listview)

        # Store DoubleSpinBox for amount edition on transaction
        self.edit_amount = QDoubleSpinBox(self.transactions_listview)

        # Store DateEdit for date edition on transaction
        self.edit_date = QDateEdit(self.transactions_listview)

        # Store Combobox for account selection on transaction
        self.edit_account = QComboBox(self.transactions_listview)

        # Store Combobox for type expense selection on transaction
        self.edit_exp_or_inc = ExpensesIncomeTransfer(self.transactions_listview)

        # Store mean widget
        self.edit_mean = Mean(self.transactions_listview)

        # Store Apply/Cancel QPushButtons when in edit mode
        self.apply = QPushButton(parent=self.transactions_listview)
        self.cancel = QPushButton(parent=self.transactions_listview)

        # Model for filtering
        self.transactions_filter_model = TransactionsFilterModel()

        # Model to handle data in transactions list
        d = [
            {
                "name": "Flunch",
                "category": "Restaurants",
                "amount": 25.99,
                "date": "20/02/2020",
                "account": "Compte Chèque",
                "type": "Income",
                "means": "Carte Bleue",
                "comment": ""
            },
            {
                "name": "Gasoil",
                "category": "Transport",
                "amount": 40.01,
                "date": "12/05/2020",
                "account": "Livret A",
                "type": "Expenses",
                "means": "Espèces",
                "comment": ""
            },
            {
                "name": "Computer",
                "category": "Groceries",
                "amount": 900.99,
                "date": "24/05/2020",
                "account": "Livret Jeune",
                "type": "Expenses",
                "means": "Virement",
                "comment": "Télétravail"
            },
            {
                "name": "Virement",
                "category": "Transfer",
                "amount": 245.00,
                "date": "22/05/2020",
                "account": "Livret Jeune",
                "type": "Transfer",
                "means": "Virement",
                "comment": "Virement vers Livret A"
            }
        ]
        self.transactions_model = TransactionsModel(d)

        # Configure edit widgets
        self.configure_edit_widgets()

        # Configure status bar
        self.configure_status_bar()

        # Configure layout
        self.configure_layout()

        # Configure List view
        self.configure_list_view()

        # Configure TitleBar
        self.configure_title_bar()

        # Connect all widgets
        self.connect_slots_and_signals()

    def connect_slots_and_signals(self):
        """
        Connect all slots and signals

        :return: None
        """

        # Connect signal from Edit button in list view to edit menu
        self.transaction_delegate.transactionEditPressed.connect(self.edit_transaction)

        # Connect signal from Delete button in list view to delete item
        self.transaction_delegate.transactionDeletePressed.connect(self.delete_transaction)

        # Connect signal from Apply button in list view to modify item
        self.transaction_delegate.transactionModified.connect(self.modify_transaction)

        # Connect signal from Cancel button in list view to abort modifications in item
        self.transaction_delegate.transactionModifCanceled.connect(self.hide_edit_widgets)

        # Connect signal from comment hovered button in list view to open menu with comment content
        self.transaction_delegate.commentHovered.connect(self.display_comment)

        # Connect signal from click/edit on +/search button
        self.ui_setup.transactions.titleBarClicked.connect(self.add_transaction)
        self.ui_setup.transactions.titleBarSearched.connect(self.search_transaction)

        # Update filtering when click on button in status bar
        self.expenses.clicked.connect(self.update_current_filtering)
        self.income.clicked.connect(self.update_current_filtering)
        self.all.clicked.connect(self.update_current_filtering)
        self.transfer.clicked.connect(self.update_current_filtering)

        # Update filtering when click on button in status bar
        self.all_account.clicked.connect(self.add_filter)
        self.account1.clicked.connect(self.add_filter)
        self.account2.clicked.connect(self.add_filter)
        self.account3.clicked.connect(self.add_filter)

    def display_comment(self, rectangle, index):
        """
        Display comment for current index

        :param rectangle: rectangle position
        :param index: current index hovered
        :return: None
        """

        pass

    def configure_edit_widgets(self):
        """
        Configure all edit widgets in transaction item

        :return: None
        """

        # Configure Name widget
        self.edit_name.setFont(QFont("Roboto", 11))
        self.edit_name.textChanged.connect(self.resize_edit_widget)
        self.edit_name.setVisible(False)

        # Configure Amount widget
        self.edit_amount.setMinimum(0.0)
        self.edit_amount.setMaximum(100000.0)
        self.edit_amount.setFont(QFont("Roboto", 11))
        self.edit_amount.valueChanged.connect(self.resize_edit_widget)
        self.edit_amount.setVisible(False)

        # Configure DateEdit widget
        self.edit_date.setFont(QFont("Roboto", 11))
        self.edit_date.setCalendarPopup(True)
        self.edit_date.setCalendarWidget(CalendarWidget())
        self.edit_date.dateChanged.connect(self.resize_edit_widget)
        self.edit_date.setVisible(False)

        # Configure ComboBox widget
        self.edit_account.setView(QListView())
        self.edit_account.setStyleSheet("QListView {"
                                        "font-size: 11pt;"
                                        "font-family: \"Roboto\";"
                                        "}"
                                        "QComboBox QAbstractItemView::item\n"
                                        "{\n"
                                        "	min-height: 25px;\n"
                                        "}\n")
        self.edit_account.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.edit_account.view().window().setAttribute(Qt.WA_TranslucentBackground)
        self.edit_account.setFont(QFont("Roboto", 11))
        self.edit_account.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.edit_account.addItems(["Livret A", "Compte Chèque", "Livret Jeune"])
        self.edit_account.setCursor(Qt.PointingHandCursor)
        self.edit_account.setVisible(False)

        # Configure custom widget
        self.edit_exp_or_inc.setVisible(False)
        self.edit_mean.setVisible(False)

        # Configure combobox/label for category
        self.edit_category.setItemDelegate(CategoryComboBox())
        self.edit_category.addItem(QIcon(":/images/images/local_grocery_store-white-18dp.svg"), "Groceries")
        self.edit_category.addItem(QIcon(":/images/images/directions_car-white-18dp_outlined.svg"), "Transport")
        self.edit_category.addItem(QIcon(":/images/images/restaurant-white-18dp_outlined.svg"), "Restaurants")
        self.edit_category.view().setSpacing(2)
        self.edit_category.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.edit_category.setCursor(Qt.PointingHandCursor)
        self.edit_category.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.edit_category.view().window().setAttribute(Qt.WA_TranslucentBackground)
        self.edit_category.setIconSize(QSize(24, 24))
        self.edit_category_name.setFont(QFont("Roboto", 10, QFont.Normal))
        self.edit_category_name.setStyleSheet("color: #75879B;")
        self.edit_category.currentTextChanged.connect(self.update_category_name)
        self.edit_category.setVisible(False)
        self.edit_category_name.setVisible(False)

        # Configure Apply/Cancel buttons
        self.apply.setIcon(QIcon(":/images/images/check-white-18dp.svg"))
        self.cancel.setIcon(QIcon(":/images/images/close-white-18dp.svg"))
        self.apply.setIconSize(QSize(18, 18))
        self.cancel.setIconSize(QSize(18, 18))
        self.apply.setCursor(Qt.PointingHandCursor)
        self.cancel.setCursor(Qt.PointingHandCursor)
        self.apply.setVisible(False)
        self.cancel.setVisible(False)
        self.apply.clicked.connect(self.modify_transaction)
        self.cancel.clicked.connect(self.hide_edit_widgets)
        self.apply.setObjectName(u"apply")
        self.cancel.setObjectName(u"cancel")

    def update_category_name(self, name: str):
        """
        Update category name
        
        :param name: name
        :return: None
        """

        # Set text
        self.edit_category_name.setText(name)

        # Update width according to text
        font_metrics = QFontMetrics(self.edit_category_name.font())
        pixels_width = font_metrics.width(self.edit_category_name.text())
        self.edit_category_name.setFixedWidth(pixels_width)

    def edit_transaction(self, index, rectName: QRect, rectAmount: QRect, rectDate: QRect, rectAccount: QRect,
                         rectExpOrInc: QRect, rectCategory: QRect,
                         rectCategoryName: QRect, rect_mean: QRect, rectEdit: QRect, rectDelete: QRect):
        """
        Edit transaction on Edit click

        :param index: item's index
        :param rectName: rect where to put LineEdit
        :param rectAmount: rect where to put DoubleSpinBox
        :param rectDate: rect where to put DateEdit
        :param rectAccount: rect where to put Combobox
        :param rectExpOrInc: rect where to put ExpOrInc
        :param rectCategory: rect where to put Category
        :param rectCategoryName: rect where to put Category Name
        :param rect_mean: rect where to put Means button
        :param rectEdit: rect where to put Apply button
        :param rectDelete: rect where to put Cancel button
        :return: None
        """

        # Disable selection
        self.transactions_listview.setSelectionMode(QAbstractItemView.NoSelection)

        # Configure Name widget
        self.edit_name.setText(self.transactions_filter_model.data(index, Qt.DisplayRole)["name"])
        font_metrics = QFontMetrics(self.edit_name.font())
        pixels_width = font_metrics.width(self.edit_name.text())
        pixels_height = font_metrics.height()
        self.edit_name.setGeometry(rectName.x(), rectName.y() - 3, pixels_width + 10, pixels_height + 6)
        self.edit_name.setVisible(True)

        # Configure ComboBox/Label widget
        selected_category = self.transactions_filter_model.data(index, Qt.DisplayRole)["category"]
        if selected_category == '':
            self.edit_category.setCurrentIndex(-1)
        else:
            self.edit_category_name.setText(selected_category)
        self.edit_category.setGeometry(rectCategory.x(), rectCategory.y(), rectCategory.width(), rectCategory.height())
        self.edit_category_name.setGeometry(rectCategoryName.x(), rectCategoryName.y(), rectCategoryName.width(),
                                            rectCategoryName.height())
        self.edit_category.setVisible(True)
        self.edit_category_name.setVisible(True)

        # Configure Amount widget
        amount = self.transactions_filter_model.data(index, Qt.DisplayRole)["amount"]
        self.edit_amount.setValue(amount)
        font_metrics = QFontMetrics(self.edit_amount.font())
        pixels_width = font_metrics.width(str(self.edit_amount.value()))
        pixels_height = font_metrics.height()
        self.edit_amount.setGeometry(rectAmount.x(), rectAmount.y() - 3, pixels_width + 38, pixels_height + 6)
        self.edit_amount.setVisible(True)

        # Configure DateEdit widget
        date_str = self.transactions_filter_model.data(index, Qt.DisplayRole)["date"]
        self.edit_date.setDate(QDate.fromString(date_str, 'dd/MM/yyyy'))
        font_metrics = QFontMetrics(self.edit_date.font())
        pixels_width = font_metrics.width(self.edit_date.date().toString('dd/MM/yyyy'))
        pixels_height = font_metrics.height()
        self.edit_date.setGeometry(rectDate.x(), rectDate.y() - 3, pixels_width + 30, pixels_height + 6)
        self.edit_date.setVisible(True)

        # Configure ComboBox widget
        selected_account = self.transactions_filter_model.data(index, Qt.DisplayRole)["account"]
        self.edit_account.setCurrentText(selected_account)
        self.edit_account.move(rectAccount.x(), rectAccount.y() - 3)
        self.edit_account.setVisible(True)

        # Configure Custom widget
        selected_exp_or_inc = self.transactions_filter_model.data(index, Qt.DisplayRole)["type"]
        self.edit_exp_or_inc.move(rectExpOrInc.x() - 4, self.edit_category.y())
        self.edit_exp_or_inc.setFixedWidth(rectExpOrInc.width() + 9)
        self.edit_exp_or_inc.setFixedHeight(self.edit_category.height())
        self.edit_exp_or_inc.set_active_type(selected_exp_or_inc)
        self.edit_exp_or_inc.setVisible(True)

        # Configure Mean widget
        mean = self.transactions_filter_model.data(index, Qt.DisplayRole)["means"]
        self.edit_mean.move(rect_mean.x() - rect_mean.width() - 10, rect_mean.y() - 5)
        self.edit_mean.setFixedWidth(rect_mean.width() * 3 + 20)
        self.edit_mean.setFixedHeight(rect_mean.height() + 10)
        self.edit_mean.set_active_type(mean)
        self.edit_mean.setVisible(True)

        # Configure Apply/Cancel buttons
        self.apply.setGeometry(rectEdit)
        self.cancel.setGeometry(rectDelete)
        self.apply.setVisible(True)
        self.cancel.setVisible(True)

    def resize_edit_widget(self):
        """
        Resize sender object (width especially) according to typed content
        :return: None
        """

        sender = self.sender()
        font_metrics = QFontMetrics(sender.font())

        if isinstance(sender, QLineEdit):
            value = sender.text()
            pixelsWidth = font_metrics.width(value)
            sender.setFixedWidth(pixelsWidth + 12)
        elif isinstance(sender, QDoubleSpinBox):
            value = str(sender.value())
            pixelsWidth = font_metrics.width(value)
            sender.setFixedWidth(pixelsWidth + 38)
        elif isinstance(sender, QDateEdit):
            value = str(sender.date().toString('dd/MM/yyyy'))
            pixelsWidth = font_metrics.width(value)
            sender.setFixedWidth(pixelsWidth + 30)

    def delete_transaction(self, index):
        """
        Delete transaction on Delete click
        :param index: index in model
        :return: None
        """

        # Remove transaction from model
        self.transactions_filter_model.delete_transaction(index)

    def add_transaction(self):
        """
        Add transaction on + click
        :return: None
        """

        # Add transaction to model
        self.transactions_filter_model.add_transaction()

        # Set editable mode
        index = self.transactions_filter_model.index(0, 0)
        self.transaction_delegate.set_editable(index)

        # Select line
        selection_model = self.transactions_listview.selectionModel()
        selection_model.select(index, QItemSelectionModel.ClearAndSelect)
        self.transactions_listview.setSelectionMode(QAbstractItemView.NoSelection)

        # Retrieve all rects
        output = self.transaction_delegate.get_first_row_rects()
        self.edit_transaction(index, output[0], output[1], output[2], output[3], output[4], output[5], output[6],
                              output[7], output[8], output[9])

    def search_transaction(self, content: str, search_field: str):
        """
        Search transaction as filter

        :param content: content to look for in transactions
        :param search_field: search field
        :return: None
        """

        # Look for name/date/amount
        if "name" in search_field.lower():
            # Filter model
            self.transactions_filter_model.update_search_filter("name", content)
        elif "date" in search_field.lower():
            # Filter model
            self.transactions_filter_model.update_search_filter("date", content)
        elif "amount" in search_field.lower():
            # Filter model
            self.transactions_filter_model.update_search_filter("amount", content)
        else:
            # Reset filter model
            self.transactions_filter_model.update_search_filter(None, None)

    def modify_transaction(self, index):
        """
        Modify transaction content on Apply click

        :param index: index in model
        :return: None
        """

        value = {"name": self.edit_name.text(), "category": self.edit_category_name.text(),
                 "amount": self.edit_amount.value(), "date": self.edit_date.date().toString("dd/MM/yyyy"),
                 "account": self.edit_account.currentText(), "type": self.edit_exp_or_inc.active_type(),
                 "means": self.edit_mean.active_type(), "comment": ""}

        # Remove transaction from model """
        self.transactions_filter_model.modify_transaction(self.transaction_delegate.editable, value)

        # TODO: to remove
        # rest_client = RestClient().POST("http://127.0.0.1:8000/dashboard/transaction/", value)

        # Hide editable widgets """
        self.hide_edit_widgets()

    def hide_edit_widgets(self):
        """
        Hide all editable widgets in transaction item

        :return: None
        """

        # Hide all widgets """
        self.edit_name.setVisible(False)
        self.edit_amount.setVisible(False)
        self.edit_date.setVisible(False)
        self.edit_account.setVisible(False)
        self.edit_exp_or_inc.setVisible(False)
        self.edit_mean.setVisible(False)
        self.edit_category.setVisible(False)
        self.edit_category_name.setVisible(False)
        self.apply.setVisible(False)
        self.cancel.setVisible(False)

        # Re-enable selection """
        self.transactions_listview.setSelectionMode(QAbstractItemView.SingleSelection)

        # Clear selection """
        selection_model = self.transactions_listview.selectionModel()
        selection_model.select(self.transaction_delegate.editable, QItemSelectionModel.Clear)

        # Disable editable state """
        self.transaction_delegate.set_editable(False)

    def configure_layout(self):
        """
        Configure layout inside of Container

        :return: None
        """

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.transactions_listview)
        layout.addWidget(self.status_bar)
        layout.setContentsMargins(0, 10, 0, 0)

        self.ui_setup.transactions.setWidget(widget)

    def configure_list_view(self):
        """
        Configure transactions list view to handle events/model

        :return: None
        """

        # Set proxy model """
        self.transactions_filter_model.setSourceModel(self.transactions_model)

        # Date re-filtered if model changed """
        self.transactions_filter_model.setDynamicSortFilter(True)
        self.transactions_filter_model.sort(0, Qt.DescendingOrder)

        # Set model """
        self.transactions_listview.setModel(self.transactions_filter_model)

        # Set mouse tracking """
        self.transactions_listview.setMouseTracking(True)

        # Set item delegate"""
        self.transactions_listview.setItemDelegate(self.transaction_delegate)

        # Hide widgets for edition """
        self.edit_name.setVisible(False)
        self.edit_amount.setVisible(False)
        self.edit_date.setVisible(False)

    def configure_status_bar(self):
        """
        Configure status bar

        :return: None
        """

        # Set states for activation """
        self.all.setProperty("activated", "true")
        self.all.update()
        self.expenses.setProperty("activated", "false")
        self.expenses.update()
        self.income.setProperty("activated", "false")
        self.income.update()
        self.transfer.setProperty("activated", "false")
        self.transfer.update()

        # Set states for activation """
        self.all_account.setProperty("activated", "true")
        self.all_account.update()
        self.account1.setProperty("activated", "false")
        self.account1.update()
        self.account2.setProperty("activated", "false")
        self.account2.update()
        self.account3.setProperty("activated", "false")
        self.account3.update()

        # Set cursor for left buttons """
        self.all.setCursor(Qt.PointingHandCursor)
        self.expenses.setCursor(Qt.PointingHandCursor)
        self.expenses.setIconSize(QSize(18, 18))
        self.expenses.setIcon(QIcon(":/images/images/hdr_weak_black_18dp_expenses.svg"))
        self.income.setCursor(Qt.PointingHandCursor)
        self.income.setIconSize(QSize(18, 18))
        self.income.setIcon(QIcon(":/images/images/hdr_weak_black_18dp_income.svg"))
        self.transfer.setCursor(Qt.PointingHandCursor)
        self.transfer.setIconSize(QSize(18, 18))
        self.transfer.setIcon(QIcon(":/images/images/hdr_weak_black_18dp_transfer.svg"))

        # Set cursor for left buttons """
        self.all_account.setCursor(Qt.PointingHandCursor)
        self.account1.setCursor(Qt.PointingHandCursor)
        self.account2.setCursor(Qt.PointingHandCursor)
        self.account3.setCursor(Qt.PointingHandCursor)

        # Add custom status bar to classic one """
        self.status_bar.addPermanentWidget(self.custom_status_bar)

        # Add buttons on left corner """
        self.status_bar.addWidget(self.all)
        self.status_bar.addWidget(self.expenses)
        self.status_bar.addWidget(self.income)
        self.status_bar.addWidget(self.transfer)

        # Add separator """
        vline = QFrame()
        vline.setFrameShape(vline.VLine)
        vline.setFixedHeight(self.all.sizeHint().height() * 1.2)
        vline.setStyleSheet("color: #344457;")
        self.status_bar.addWidget(vline)

        # Add buttons on left corner """
        self.status_bar.addWidget(self.all_account)
        self.status_bar.addWidget(self.account1)
        self.status_bar.addWidget(self.account2)
        self.status_bar.addWidget(self.account3)

        # Disable size grip """
        self.status_bar.setSizeGripEnabled(False)

        # Hide settings """
        self.custom_status_bar.hide_settings()

    def configure_title_bar(self):
        """
        Configure TitleBar with icon

        :return: None
        """

        # Set title
        self.ui_setup.transactions.set_title(QCoreApplication.translate("transactions", "Transactions"))
        self.ui_setup.transactions.set_button_tooltip(QCoreApplication.translate("transactions", "Add transaction"))

    def update_current_filtering(self):
        """
        Update current filtering after click on button

        :return: None
        """

        # Retrieve sender
        py_object = self.sender()

        # Retrieve current text
        new_filter = py_object.text()

        # Update filter
        self.transactions_filter_model.update_filter(new_filter)

        # Update activated state
        if new_filter in {'All', 'Tout'}:
            self.all.setProperty("activated", "true")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "false")
            self.transfer.setProperty("activated", "false")
        elif new_filter in {'Expenses', 'Dépenses'}:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "true")
            self.income.setProperty("activated", "false")
            self.transfer.setProperty("activated", "false")
        elif new_filter in {'Income', 'Revenus'}:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "true")
            self.transfer.setProperty("activated", "false")
        else:
            self.all.setProperty("activated", "false")
            self.expenses.setProperty("activated", "false")
            self.income.setProperty("activated", "false")
            self.transfer.setProperty("activated", "true")

        # Update style
        self.all.style().unpolish(self.all)
        self.all.style().polish(self.all)
        self.expenses.style().unpolish(self.expenses)
        self.expenses.style().polish(self.expenses)
        self.income.style().unpolish(self.income)
        self.income.style().polish(self.income)
        self.transfer.style().unpolish(self.transfer)
        self.transfer.style().polish(self.transfer)

    def add_filter(self):
        """
        Add filter to current filtering after click on button

        :return: None
        """

        # Retrieve sender
        py_object = self.sender()

        # Retrieve current text
        new_filter = py_object.text()

        # Add filter
        self.transactions_filter_model.add_filter(new_filter)

        # Update activated state
        if new_filter == 'All':
            self.all_account.setProperty("activated", "true")
            self.account1.setProperty("activated", "false")
            self.account2.setProperty("activated", "false")
            self.account3.setProperty("activated", "false")
        elif new_filter == self.account1.text():
            self.all_account.setProperty("activated", "false")
            self.account1.setProperty("activated", "true")
            self.account2.setProperty("activated", "false")
            self.account3.setProperty("activated", "false")
        elif new_filter == self.account2.text():
            self.all_account.setProperty("activated", "false")
            self.account1.setProperty("activated", "false")
            self.account2.setProperty("activated", "true")
            self.account3.setProperty("activated", "false")
        elif new_filter == self.account3.text():
            self.all_account.setProperty("activated", "false")
            self.account1.setProperty("activated", "false")
            self.account2.setProperty("activated", "false")
            self.account3.setProperty("activated", "true")

        # Update style
        self.all_account.style().unpolish(self.all_account)
        self.all_account.style().polish(self.all_account)
        self.account1.style().unpolish(self.account1)
        self.account1.style().polish(self.account1)
        self.account2.style().unpolish(self.account2)
        self.account2.style().polish(self.account2)
        self.account3.style().unpolish(self.account3)
        self.account3.style().polish(self.account3)
