from rest_framework import serializers
from .models import Statistics_consumption

class StatisticsConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics_consumption
        fields = '__all__'