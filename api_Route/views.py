from rest_framework import viewsets
from .serializer import RouteSerializer
from .models import Route


class RouteViewSet(viewsets.ModelViewSet):
   queryset = Route.objects.all()
   serializer_class = RouteSerializer