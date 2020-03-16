from django.contrib import admin
from . import models

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DailyStockPrice)
class DailyStockPriceAdmin(admin.ModelAdmin):
    pass
