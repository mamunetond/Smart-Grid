from rest_framework import viewsets
from .serializers import ElectricVehicleSerializer
from .models import ElectricVehicle

class ElectricVehicleViewSet(viewsets.ModelViewSet):
   queryset = ElectricVehicle.objects.all()
   serializer_class = ElectricVehicleSerializer
