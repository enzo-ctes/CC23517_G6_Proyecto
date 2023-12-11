from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    integrantes = About.objects.all()
    return render(request, "about/about.html", {'integrantes':integrantes})