from django.urls import path, include
from rest_framework import routers
from api_Statistics_consumption import views

router=routers.DefaultRouter()
router.register(r'routes', views.StatisticsConsumptionViewSet)

urlpatterns = [
    path('',include(router.urls)),
]