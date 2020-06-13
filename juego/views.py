from django.shortcuts import render
from juego.forms import UserForm
from juego.models import User
from django import forms


def index(request):
	return render(request,('juego/principal.html'))
# Create your views here.
def registrarse(request):

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
