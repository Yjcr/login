from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('casa', views.home, name = 'home'),
    path('hola', views.hola), 
    path('sign_up', views.sign_up, name = 'signup'),
    path('ver_tareas', views.tasks, name = 'tare'),
    path('log_out', views.cerrar_sesion, name = 'logoutt'),
    path('sign_in', views.inicio_sesion, name = 'signinn')
]
