"""
URL configuration for webpersonal17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as views_core
from portfolio import views as portfolio_views
from Indumentaria import views as indumentaria_views
from about import views as about_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_core.home, name='home'),
    path('about', about_views.about, name='about'),
    path('portfolio', portfolio_views.portfolio, name='portfolio'),
    path('indumentaria', indumentaria_views.indumentaria, name='indumentaria'),
    path('contact', views_core.contact, name='contact')    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)