# serializers.py

from rest_framework import serializers

class RutasOptimasSerializer(serializers.Serializer):
    rutas = serializers.ListField(child=serializers.DictField())
    ruta_optima = serializers.DictField()

    def to_representation(self, instance):
        return {
            'rutas': instance['rutas'],
            'ruta_optima': instance.get('ruta_optima', None)
        }
