from django.urls import path
from .views import RutaOptimaView

urlpatterns = [
    path('ruta_optima/', RutaOptimaView.as_view(), name='ruta_optima'),
]
