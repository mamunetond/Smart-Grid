from rest_framework import viewsets
from .serializer import ElectricVehicleSerializer
from .models import ElectricVehicle


class ChargePointViewSet(viewsets.ModelViewSet):
   queryset = ElectricVehicle.objects.all()
   serializer_class = ElectricVehicleSerializer
