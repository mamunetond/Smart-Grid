from django.urls import path
from .views import ChargePointView

urlpatterns = [
    path('charge/', ChargePointView.as_view(),name='charge_list'),
    path('charge/<int:id>', ChargePointView.as_view(),name='charge_process')
]
