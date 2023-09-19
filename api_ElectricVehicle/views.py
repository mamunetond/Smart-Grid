from rest_framework import viewsets
from .serializer import ElectricVehicleSerializer
from .models import ElectricVehicle


class ElectricVehicleViewSet(viewsets.ModelViewSet):
   queryset = ElectricVehicle.objects.all()
   serializer_class = ElectricVehicleSerializer
