from django.shortcuts import render
from juego.forms import UserForm
from juego.models import User
from django import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
	context = {}
	if request.GET.get('invalid_credentials'):
		context['invalid_credentials'] = 'Los datos no son válidos.'
	if request.user.is_authenticated:
		template_a_mostrar = 'juego/principal.html'
	else:
		template_a_mostrar = 'juego/login.html'
	return render(request, template_a_mostrar, context=context)

def registrar_usuario(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	user_form = UserForm()
	return render(request, 'juego/registration.html',context={'user_form':user_form,'registered':registered} )


def user_login(request):
	if request.method != 'POST':
		# Solo POST esta soportado (cuando se quieren autenticar).
		return HttpResponseBadRequest()
	username = request.POST.get('username')
	password = request.POST.get('password')
	autenticacion_satisfactoria = False
	user = authenticate(username=username,password=password)
	if user and user.is_active:
		login(request,user)
		autenticacion_satisfactoria = True
	error = ""
	if not autenticacion_satisfactoria:
		error = '?invalid_credentials=True'
	return HttpResponseRedirect(reverse('index') + error)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
