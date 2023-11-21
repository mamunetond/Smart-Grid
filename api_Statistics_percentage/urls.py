from django.urls import path, include
from rest_framework import routers
from api_Statistics_percentage import views

router=routers.DefaultRouter()
router.register(r'routes', views.StaticsPercentageViewSet)

urlpatterns = [
    path('',include(router.urls)),
]