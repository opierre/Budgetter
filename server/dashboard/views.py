from rest_framework.viewsets import ModelViewSet

from dashboard.models import Transaction, Bank, Account, Category
from dashboard.serializers import TransactionSerializer, BankSerializer, AccountSerializer, CategorySerializer


class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TopCategoriesViewSet(ModelViewSet):
    queryset = Category.objects.annotate()[:6]
    serializer_class = TransactionSerializer
