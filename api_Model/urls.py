from django.urls import path
from .views import ruta_optima_view

urlpatterns = [
    path('ruta_optima/', ruta_optima_view, name='ruta_optima'),
]
