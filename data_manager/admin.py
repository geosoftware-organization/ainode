from django.contrib import admin
from . import models

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Share)
class ShareAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DailyStockPrice)
class DailyStockPriceAdmin(admin.ModelAdmin):
    pass
