from rest_framework import viewsets
from .serializer import ChargePointSerializer
from .models import ChargePoint


class ChargePointViewSet(viewsets.ModelViewSet):
   queryset = ChargePoint.objects.all()
   serializer_class = ChargePointSerializer
