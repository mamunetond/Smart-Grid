from django.db import models

# Create your models here.

class Trip(models.Model):
    vehiculo_id = models.CharField(max_length=100)
    ruta1_id = models.CharField(max_length=100)
    ruta2_id = models.CharField(max_length=100)
    ruta3_id = models.CharField(max_length=100)
    distancia1 = models.IntegerField()
    distancia2 = models.IntegerField()
    distancia3 = models.IntegerField()
    duracion1 = models.IntegerField()
    duracion2 = models.IntegerField()
    duracion3 = models.IntegerField()
    consumo_ajustado1 = models.IntegerField()
    consumo_ajustado2 = models.IntegerField()
    consumo_ajustado3 = models.IntegerField()
    porcentaje_bateria1 = models.IntegerField()
    porcentaje_bateria2 = models.IntegerField()
    porcentaje_bateria3 = models.IntegerField()
    #rutas = models.JSONField()  # Almacena un arreglo de rutas
    rutas = [
        (ruta1_id,distancia1,duracion1,consumo_ajustado1,porcentaje_bateria1),
        (ruta2_id,distancia2,duracion1,consumo_ajustado2,porcentaje_bateria2),
        (ruta3_id,distancia3,duracion3,consumo_ajustado3,porcentaje_bateria3),
    ]
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
