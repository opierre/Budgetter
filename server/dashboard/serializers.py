from rest_framework.serializers import ModelSerializer

from dashboard.models import Transaction, Bank, Account, TopCategory


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class TopCategorySerializer(ModelSerializer):

    class Meta:
        model = TopCategory
        fields = '__all__'
