from django.contrib import admin
from django.urls import path, include
from juego import views

urlpatterns = [
    path("",views.index,name='index'),
    path('registration/',views.registrarse,name='registrarse')
]
