from django.shortcuts import render
from .models import Indumentaria

# Create your views here.
def indumentaria(request):
    indumentarias = Indumentaria.objects.all()
    return render(request, "Indumentaria/Indumentaria.html", {'indumentarias':indumentarias})