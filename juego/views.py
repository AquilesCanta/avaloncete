from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
	username = request.COOKIES.get('username')
	if username is None:
		username = "Desconocido"
	return render(request, 'juego/principal.html',
		context={"username": username})

def username(request):
	if request.method == 'POST':
		response = redirect('/')
		response.set_cookie("username", request.POST.get("name"))
		return response
	else:
		return render(request, 'juego/username.html')

