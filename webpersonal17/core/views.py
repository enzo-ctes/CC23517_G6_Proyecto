from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "core/home.html")

# def about(request):
#     # return HttpResponse(html_base + "<h2>Acerca de</h2><p>Soy Enzo Ramirez</p>")
#     return render(request, "core/about.html")

def contact(request):
    # return HttpResponse(html_base + "<h2>Contacto</h2><p>email: enzoctess@gmail.com</p>")
    return render(request, "core/contact.html")

# def portfolio(request):
#     return render(request, "core/portfolio.html")

# def indumentaria(request):    
#     return render(request, "core/Indumentaria.html")