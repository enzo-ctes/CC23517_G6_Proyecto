from django.shortcuts import render
from .models import Indumentaria

# Create your views here.
def indumentaria(request):
    indumentarias = Indumentaria.objects.all()
    return render(request, "Indumentaria/Indumentaria.html", {'indumentarias':indumentarias})

def indumentariasNuevas(request):   
    indumentariasNuevas = Indumentaria.objects.filter(historico=False)   
    return render(request, "Indumentaria/Indumentaria.html", {'indumentariaNueva': indumentariasNuevas})

def indumentariasHistoricas(request):
    indumentariasHistoricas = Indumentaria.objects.filter(historico=True)      
    return render(request, "Indumentaria/Indumentaria.html", {'indumentariasHistoricas': indumentariasHistoricas})