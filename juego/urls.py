from django.contrib import admin
from django.urls import path, include
from juego import views


urlpatterns = [
    path("",views.index,name='index'),
    path('registration/',views.registrar_usuario,name='registrarse'),
    path('logout/',views.user_logout,name='logout'),
    path('login/',views.user_login,name='login'),
]
