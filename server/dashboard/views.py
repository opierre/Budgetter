from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from dashboard.models import Transaction, Bank, Account
from dashboard.serializers import TransactionSerializer, BankSerializer, AccountSerializer


class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

