from django.contrib import admin
from django.urls import path, include
from juego import views

urlpatterns = [
    path("username/",views.username),
    path("",views.index),
]
