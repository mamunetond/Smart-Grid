from rest_framework import serializers
from .models import ChargePoint

class ChargePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = '__all__'