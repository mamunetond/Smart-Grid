# serializers.py
from rest_framework import serializers

class RutaSerializer(serializers.Serializer):
    numero_ruta = serializers.IntegerField()
    distancia = serializers.CharField()
    duracion = serializers.CharField()
    consumo_ajustado = serializers.FloatField()
    porcentaje_bateria_necesario = serializers.FloatField()
    mensaje = serializers.CharField()
    informacion_ruta = serializers.JSONField()

class RutasOptimasSerializer(serializers.Serializer):
    rutas = RutaSerializer(many=True)
    ruta_optima = serializers.JSONField()

    def get_ruta_optima(self, obj):
        ruta_optima = obj.get('ruta_optima', None)
        if ruta_optima:
            # Incluye la información de la ruta en la ruta óptima
            ruta_optima["informacion_ruta"] = obj.get('informacion_ruta', {})
        return ruta_optima
