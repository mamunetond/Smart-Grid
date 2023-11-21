from django.urls import path, include
from rest_framework import routers
from api_ChargePoint import views
from .views import ChargePointDeleteView


router=routers.DefaultRouter()
router.register(r'routes', views.ChargePointViewSet)

urlpatterns = [
    path('',include(router.urls)),
]