from rest_framework import serializers
from .models import ElectricVehicle

class ElectricVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricVehicle
        fields = '__all__'