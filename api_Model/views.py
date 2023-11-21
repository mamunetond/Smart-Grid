from django.shortcuts import render

from django.http import JsonResponse
from .model_predictivo import encontrar_ruta_optima

def ruta_optima_view(request):
    origen = request.GET.get('origen')
    destino = request.GET.get('destino')
    bateria_actual = float(request.GET.get('bateria_actual', 0))

    resultado = encontrar_ruta_optima(origen, destino, bateria_actual)
    return JsonResponse(resultado, safe=False)


