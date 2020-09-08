from django.db import models



USD = 'USD Wallet'
BTC = 'Bitcoin Wallet'
types = (
    (USD, 'USD Wallet'),
    (BTC, 'Bitcoin Wallet'),
)
class Cryptoseller(models.Model):
    username = models.CharField(max_length=120, blank=True, null=True)
    balance_amount = models.CharField(max_length=120, blank=True, null=True)
    exchanger=models.CharField(max_length=120, blank=False, null=True)
    Payment_method=models.CharField(max_length=120, blank=False, null=True)
    currency=models.CharField(max_length=120, blank=False, null=True, choices= types)
    Give = models.CharField(max_length=120, blank=False, null=True)
    Get = models.CharField(max_length=120, blank=False, null=True)
    Reserve = models.CharField(max_length=120, blank=False, null=True)
    Reviews = models.CharField(max_length=120, blank=False, null=True)
