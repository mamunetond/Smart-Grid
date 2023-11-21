from rest_framework import serializers
from .models import Statistics_percentage

class StatisticsPercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics_percentage
        fields = '__all__'