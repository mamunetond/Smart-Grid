# views.py

import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RutasOptimasSerializer
from .model_predictivo import encontrar_ruta_optima

class RutaOptimaView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtén los parámetros de la solicitud
        origen = request.query_params.get('origen')
        destino = request.query_params.get('destino')
        porcentaje_bateria_actual = float(request.query_params.get('bateria_actual', 0))

        # Llama a la función encontrar_ruta_optima y obtén la respuesta
        resultado = encontrar_ruta_optima(origen, destino, porcentaje_bateria_actual)

        try:
            # Convierte la respuesta en un diccionario Python
            respuesta_dict = json.loads(resultado)
        except json.JSONDecodeError:
            # Maneja el error si la respuesta no es un JSON válido
            return Response({"error": "Error al procesar la respuesta JSON"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Serializa la respuesta utilizando el nuevo serializador
        serializer = RutasOptimasSerializer(data=respuesta_dict)

        # Valida y devuelve la respuesta JSON serializada
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            # Manejo detallado de errores de validación
            print(f"Errores de validación del serializador: {serializer.errors}")

            # Devuelve errores de validación con detalles específicos
            return Response({
                "error": "Error de validación en el serializador",
                "detalles": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
