from django.shortcuts import render
from juego.forms import UserForm
from juego.models import User
from django import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request,('juego/principal.html'))

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
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse('Esta cuenta no esta activa')
		else:
			return HttpResponseRedirect(reverse('login') + '?invalid_credentials=True')
	else:
		context = {}
		if request.GET.get('invalid_credentials'):
			context['invalid_credentials'] = 'Los datos no son válidos.'
		return render(request,'juego/login.html', context=context)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
