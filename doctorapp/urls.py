"""
URL configuration for doctorapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from patients import urls as urls_patients
from doctors import urls as urls_doctors
from bookings import urls as urls_bookings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.urls')),
    path('api/patients/', include(urls_patients)),
    path('api/doctors/', include(urls_doctors)),
    path('api/bookings/', include(urls_bookings)),
]
