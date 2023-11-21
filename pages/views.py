from typing import Any
from django import http
from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import ChargePoint, ElectricVehicle
import json
from rest_framework import generics
from .serializers import ElectricVehicleSerializer
from .utils import encontrar_ruta_optima 
# Create your views here.

class ChargePointView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if(id>0):
            chargePoints = list(ChargePoint.objects.filter(id=id).values())
            if len(chargePoints)>0:
                point = chargePoints[0]
                data = {'message':"Success", 'point':point}
            else:
                data = {'message':"not data"}
            return JsonResponse(data)
        else:
            chargePoints = list(ChargePoint.objects.values())
            if len(chargePoints)>0:
                data = {'message':"success", 'chargePoints':chargePoints}
            else:
                data = {'message':"not data"}
        return JsonResponse(data)


    def post(self, request):
        jasonData = json.loads(request.body)
        ChargePoint.objects.create(name_point=jasonData['name_point'],company=jasonData['company'], latitude=jasonData['latitude'], longitude=jasonData['longitude'])
        data = {'message':"Success"}
        return JsonResponse(data)

    def put(self, request,id):
        jasonData = json.loads(request.body)
        chargePoints = list(ChargePoint.objects.filter(id=id).values())
        if len(chargePoints)>0:
            point = ChargePoint.objects.get(id=id)
            point.name_point = jasonData['name_point']
            point.company = jasonData['company']
            point.latitude = jasonData['latitude']
            point.longitude = jasonData['longitude']
            point.save()
            data = {'message':"Success"}
        else:
            data = {'message':"not data"}
        return JsonResponse(data)
    def delete(self, request):
        pass

class ElectricVehicleListCreate(generics.ListCreateAPIView):
    queryset = ElectricVehicle.objects.all()
    serializer_class = ElectricVehicleSerializer

class ElectricVehicleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricVehicle.objects.all()
    serializer_class = ElectricVehicleSerializer
    
class ruta_optima():     
    def get(self, request, *args, **kwargs):         
        origen = request.GET.get('origen')         
        destino = request.GET.get('destino')  
        porcentaje_actual = request.GET.get('porcentaje')              
        ruta_optima = encontrar_ruta_optima(origen, destino,porcentaje_actual)        
        return JsonResponse(ruta_optima)
