from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    identification = models.IntegerField()
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    created_at_user = models.DateTimeField(auto_now=True)
    updated_at_user = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.identification


class Route(models.Model):
    tittle = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    distance = models.IntegerField()
    time = models.IntegerField()
    latitude_origin = models.IntegerField()
    latitude_destination = models.IntegerField()
    longitude_origin = models.IntegerField()
    longitude_destination = models.IntegerField()
    created_at_route = models.DateTimeField(auto_now_add=True)
    updated_at_route = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tittle