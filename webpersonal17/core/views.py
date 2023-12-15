from django.shortcuts import render, HttpResponse
from about.models import About
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def contact(request):
    integrantes = About.objects.all()
    # return HttpResponse(html_base + "<h2>Contacto</h2><p>email: enzoctess@gmail.com</p>")
    # return render(request, "core/contact.html")
    return render(request, "core/contact.html", {'integrantes':integrantes})