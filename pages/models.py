from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

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
    battery_percentage = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at_route = models.DateTimeField(auto_now_add=True)
    updated_at_route = models.DateTimeField(auto_now_add=True)
    
    def __srt__(self):
        return self.tittle

class ChargePoint(models.Model):
    name_point = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    activate = models.BooleanField()
    private = models.BooleanField()
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at_point = models.DateTimeField(auto_now_add=True)
    updated_at_point = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_point
    


class ElectricVehicle(models.Model):
    vehicle_id= models.AutoField(primary_key=True) 
    make = models.CharField(max_length=100) #The make of vehicle example tesla.
    model = models.CharField(max_length=100)# The model or reference of vehicle.
    year = models.PositiveIntegerField() # The year of manufacture of the vehicle.
    battery_capacity_kwh = models.DecimalField(max_digits=5, decimal_places=2)#The capacity of the battery in kilowatt-hours.
    range_kilometers = models.PositiveIntegerField()#The range of the vehicle in kilometers.
    charging_time_hours = models.DecimalField(max_digits=5, decimal_places=2)#The charging time in hours.
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at_electricVehicle = models.DateTimeField(auto_now_add=True)
    updated_at_electricVehicle = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    

class UserAdmin(models.Model):
    identification = models.IntegerField()
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    charge_point = models.ForeignKey(ChargePoint,on_delete=models.CASCADE)
    electric_vehicle = models.ForeignKey(ElectricVehicle,on_delete=models.CASCADE)
    created_at_user = models.DateTimeField(auto_now=True)
    updated_at_user = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.identification
    
    
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

    def _str_(self):
        return f"Viaje desde {self.origen} hasta {self.destino} para el vehículo {self.vehiculo_id}"
    
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
    

class Statistics_consumption(models.Model):
    
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
    consumo_total = models.IntegerField()
    


