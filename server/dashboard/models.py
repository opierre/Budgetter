from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    website = models.URLField()


class Account(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)


class Transaction(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    category = models.CharField(max_length=1000, blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    account = models.ForeignKey(Account, blank=False, null=True, on_delete=models.CASCADE)

    EXPENSES = 'Expenses'
    INCOME = 'Income'
    TYPE_CHOICES = [
        (EXPENSES, 'Expenses'),
        (INCOME, 'Income'),
    ]
    type = models.CharField(max_length=1000, choices=TYPE_CHOICES, default=EXPENSES)
    comment = models.CharField(max_length=1000, blank=True, null=True)


class TopCategory(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    nbTransactions = models.IntegerField(blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
