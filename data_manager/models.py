from django.db import models
SHARE = 'SHR'
COMMODITY = 'CMM'
ETF = 'ETF'
CFD = 'CFD'
INDEX = 'IDX'
CRYPTO = 'CRYPTO'
FOREX = 'FX'
STOCK_TYPES = [
    (SHARE, 'Share'),
    (COMMODITY, 'Commodity'),
    (ETF, 'Exchange Trade Funds'),
    (CFD, 'Contract for difference'),
    (INDEX, 'Hypothetical portfolio of investment holdings which \
        represents a segment of the financial market'),
    (CRYPTO, 'Crypto currencies'),
    (FOREX, 'Marketplace for a various national currencies'),
]

class Country(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} {self.code}'

class Share(models.Model):
    symbol = models.CharField(max_length=10)
    full_name = models.CharField(max_length=200)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.symbol}'

class DailyStockPrice(models.Model):
    stock = models.ForeignKey(Share, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=STOCK_TYPES, default=SHARE)
    date = models.DateField()
    open_price = models.DecimalField(decimal_places=5, max_digits=19, null=True, blank=True)
    high_price = models.DecimalField(decimal_places=5, max_digits=19, null=True, blank=True)
    low_price = models.DecimalField(decimal_places=5, max_digits=19, null=True, blank=True)
    close_price = models.DecimalField(decimal_places=5, max_digits=19, null=True, blank=True)

    def is_currency(self):
        return self.type in {FOREX, CRYPTO}



