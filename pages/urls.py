from django.urls import path,include
from .views import ChargePointView
from django.contrib import admin

urlpatterns = [
    path('charge/', ChargePointView.as_view(),name='charge_list'),
    path('charge/<int:id>', ChargePointView.as_view(),name='charge_process'),
]
