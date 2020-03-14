from rest_framework import serializers
from . import models

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Share
        fields = '__all__'

class DailyStockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyStockPrice
        fields = '__all__'
