from django.urls import path, include
from rest_framework import routers
from api_ElectricVehicle import views

router=routers.DefaultRouter()
router.register(r'routes', views.ElectricVehicleViewSet)

urlpatterns = [
    path('',include(router.urls)),
]