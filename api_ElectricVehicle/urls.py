from django.urls import path, include
from rest_framework import routers
from .views import ElectricVehicleViewSet

router = routers.DefaultRouter()
router.register(r'routes', ElectricVehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
