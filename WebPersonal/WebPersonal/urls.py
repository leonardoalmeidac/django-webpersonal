"""WebPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from core import views as core_views
from servicios import views as servicios_views 
from contact import views as contact_views

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('services/', servicios_views.servicios, name="services"),
    path('contact-us/', core_views.contact, name="contact"),
    path('info/', contact_views.infoform, name="infodata"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG :
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
