# serializers.py
from rest_framework import serializers

class RutaSerializer(serializers.Serializer):
    numero_ruta = serializers.IntegerField()
    distancia = serializers.CharField()
    duracion = serializers.CharField()
    consumo_ajustado = serializers.FloatField()
    porcentaje_bateria_necesario = serializers.FloatField()
    porcentaje_recargar = serializers.FloatField()
    necesita_recargar = serializers.BooleanField()
    ruta_optima = serializers.BooleanField()
    informacion_ruta = serializers.JSONField()

class RutasOptimasSerializer(serializers.Serializer):
    rutas = RutaSerializer(many=True)

    def to_representation(self, instance):
        # Elimina el campo "ruta_optima" si existe
        if "ruta_optima" in instance:
            del instance["ruta_optima"]
        return super().to_representation(instance)