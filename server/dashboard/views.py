from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet

from dashboard.models import Transaction, Bank, Account
from dashboard.serializers import TransactionSerializer, BankSerializer, AccountSerializer, TopCategorySerializer


class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TopCategoriesViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TopCategorySerializer

    def get_queryset(self):

        if ('year' and 'month') in self.request.GET:
            year = self.request.GET['year']
            month = self.request.GET['month']

            query_set = Transaction.objects.filter(date__year=year, date__month=month)
            query_set = query_set.values('category').aggregate(Sum('amount'))

            return query_set