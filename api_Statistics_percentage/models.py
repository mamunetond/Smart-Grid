from django.db import models

# Create your models here.

class Statistics_percentage(models.Model):
    
    Statistics_id = models.IntegerField()
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
