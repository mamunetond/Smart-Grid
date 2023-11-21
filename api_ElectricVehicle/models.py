from django.db import models

class ElectricVehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True) 
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    battery_capacity_kwh = models.DecimalField(max_digits=5, decimal_places=2)
    range_kilometers = models.PositiveIntegerField()
    charging_time_hours = models.DecimalField(max_digits=5, decimal_places=2)
    created_at_electricVehicle = models.DateTimeField(auto_now_add=True)
    updated_at_electricVehicle = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
