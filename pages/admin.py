from django.contrib import admin
from .models import UserAdmin, Route, ChargePoint,ElectricVehicle
# Register your models here.

admin.site.register(UserAdmin)
admin.site.register(Route)
admin.site.register(ChargePoint)
admin.site.register(ElectricVehicle)
