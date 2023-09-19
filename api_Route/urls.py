from django.urls import path, include
from rest_framework import routers
from api_Route import views

router=routers.DefaultRouter()
router.register(r'routes', views.RouteViewSet)

urlpatterns = [
    path('',include(router.urls)),
]