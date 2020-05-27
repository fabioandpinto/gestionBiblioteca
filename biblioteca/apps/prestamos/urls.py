from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'n-prestamo/',
        views.NuevoPrestamo.as_view(),
        name='n-prestamo')
]
