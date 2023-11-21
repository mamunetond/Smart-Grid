from django.db import models

# Create your models here.

class Trip(models.Model):
    vehiculo_id = models.CharField(max_length=100)
    ruta_id = models.CharField(max_length=100)
    distancia = models.IntegerField()
    duracion = models.IntegerField()
    consumo_ajustado = models.IntegerField()
    porcentaje_bateria = models.IntegerField()
    #rutas = models.JSONField()  # Almacena un arreglo de rutas
    rutas = [
        (ruta_id,distancia,duracion,consumo_ajustado,porcentaje_bateria),
    ]
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    Statistics_id = models.IntegerField()
    fecha = models.DateField()
    Enero = models.IntegerField()
    Febrero = models.IntegerField()
    Marzo = models.IntegerField()
    Abril = models.IntegerField()
    Mayo = models.IntegerField()
    Junio = models.IntegerField()
    Julio = models.IntegerField()
    Agosto = models.IntegerField()
    Septiembre = models.IntegerField()
    Octubre = models.IntegerField()
    Noviembre = models.IntegerField()
    Diciembre = models.IntegerField()
    porcentaje_consumido = models.IntegerField()
    carga_restante = models.IntegerField()
    consumo_total = models.IntegerField()
