from django.shortcuts import render
from .models import Service

# Create your views here.

def servicios(request) :
    #crear array de servicios
    servicios = Service.objects.all()
    return render(request, 'servicios/services.html', {'servicio' : servicios}) 