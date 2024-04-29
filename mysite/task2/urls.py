from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.registro),
    path('hola', views.hola, name='hi')
]
