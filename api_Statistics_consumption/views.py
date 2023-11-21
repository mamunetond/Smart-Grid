from rest_framework import viewsets
from .serializer import StatisticsConsumptionSerializer
from .models import Statistics_consumption


class StatisticsConsumptionViewSet(viewsets.ModelViewSet):
   queryset = Statistics_consumption.objects.all()
   serializer_class = StatisticsConsumptionSerializer