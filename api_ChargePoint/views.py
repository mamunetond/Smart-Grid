from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializer import ChargePointSerializer
from .models import ChargePoint

class ChargePointViewSet(viewsets.ModelViewSet):
    queryset = ChargePoint.objects.all()
    serializer_class = ChargePointSerializer

class ChargePointDeleteView(generics.DestroyAPIView):
   queryset = ChargePoint.objects.all()
   serializer_class = ChargePointSerializer
