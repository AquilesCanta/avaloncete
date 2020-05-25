from django.shortcuts import render


def index(request):
	return render(request,('juego/principal.html'))
# Create your views here.
