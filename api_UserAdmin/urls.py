from django.urls import path, include
from rest_framework import routers
from api_UserAdmin import views

router=routers.DefaultRouter()
router.register(r'useradmins', views.UserAdminViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
