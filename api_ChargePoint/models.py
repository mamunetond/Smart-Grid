from django.db import models

# Create your models here.

class ChargePoint(models.Model):
    name_point = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    activate = models.BooleanField()
    private = models.BooleanField()
    address = models.CharField(max_length=200)
    created_at_point = models.DateTimeField(auto_now_add=True)
    updated_at_point = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_point
