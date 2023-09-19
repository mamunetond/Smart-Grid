from rest_framework import serializers
from .models import UserAdmin

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = '__all__'
        