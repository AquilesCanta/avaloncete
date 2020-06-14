from juego.models import UsuarioAvaloncete
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Confirmar Contraseña')
    username = forms.CharField(label='Usuario')

    class Meta():
        model = User
        fields = ('username','password','password2')
