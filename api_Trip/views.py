from rest_framework import viewsets
from .serializer import TripSerializer
from .models import Trip


class TripViewSet(viewsets.ModelViewSet):
   queryset = Trip.objects.all()
   serializer_class = TripSerializer