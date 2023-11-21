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
    ruta_optima = serializers.BooleanField()

class RutasOptimasSerializer(serializers.Serializer):
    rutas = RutaSerializer(many=True)

    def to_representation(self, instance):
        # Custom representation to remove the 'ruta_optima' field if it is None
        data = super().to_representation(instance)
        data.pop("ruta_optima", None)
        return data
