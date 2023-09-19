from django.db import models

# Create your models here.

class ElectricVehicle(models.Model):
    vehicle_id= models.AutoField(primary_key=True) 
    make = models.CharField(max_length=100) #The make of vehicle example tesla.
    model = models.CharField(max_length=100)# The model or reference of vehicle.
    year = models.PositiveIntegerField() # The year of manufacture of the vehicle.
    battery_capacity_kwh = models.DecimalField(max_digits=5, decimal_places=2)#The capacity of the battery in kilowatt-hours.
    range_kilometers = models.PositiveIntegerField()#The range of the vehicle in kilometers.
    charging_time_hours = models.DecimalField(max_digits=5, decimal_places=2)#The charging time in hours.
    created_at_electricVehicle = models.DateTimeField(auto_now_add=True)
    updated_at_electricVehicle = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
