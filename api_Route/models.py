from django.db import models

# Create your models here.

class Route(models.Model):
    tittle = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    distance = models.IntegerField()
    time = models.IntegerField()
    latitude_origin = models.FloatField()
    latitude_destination = models.FloatField()
    longitude_origin = models.FloatField()
    longitude_destination = models.FloatField()
    created_at_route = models.DateTimeField(auto_now_add=True)
    updated_at_route = models.DateTimeField(auto_now_add=True)
