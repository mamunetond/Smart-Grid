from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserAdmin(models.Model):
    identification = models.IntegerField()
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    created_at_user = models.DateTimeField(auto_now=True)
    updated_at_user = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.identification



