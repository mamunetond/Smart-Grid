from django.urls import path, include
from rest_framework import routers
from api_Trip import views

router=routers.DefaultRouter()
router.register(r'routes', views.TripViewSet)

urlpatterns = [
    path('',include(router.urls)),
]