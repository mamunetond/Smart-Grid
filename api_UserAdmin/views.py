from rest_framework import viewsets
from .serializer import UserAdminSerializer
from .models import UserAdmin


class UserAdminViewSet(viewsets.ModelViewSet):
   queryset = UserAdmin.objects.all()
   serializer_class = UserAdminSerializer
   