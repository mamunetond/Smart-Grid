from rest_framework import viewsets
from .serializer import StatisticsPercentageSerializer
from .models import Statistics_percentage


class StaticsPercentageViewSet(viewsets.ModelViewSet):
   queryset = Statistics_percentage.objects.all()
   serializer_class = StatisticsPercentageSerializer