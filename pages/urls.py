from django.urls import path,include
from .views import ChargePointView
from . import views
from django.contrib import admin
from .views import ruta_optima

urlpatterns = [
    path('charge/', ChargePointView.as_view(),name='charge_list'),
    path('charge/<int:id>', ChargePointView.as_view(),name='charge_process'),
    path('vehicles/', views.ElectricVehicleListCreate.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', views.ElectricVehicleRetrieveUpdateDestroy.as_view(), name='vehicle-detail'),
    path('ruta-optima/', ruta_optima.as_view(), name='ruta-optima'),
]
