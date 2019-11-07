from django import forms

from .models import *

class AutoForm(forms.ModelForm):
	class Meta:
		model = Autor
		exclude = ['id_autor']

class EntradaForm(forms.ModelForm):
	
	class Meta:
		model = Entrada
		fields = ['id_entrada', 'fecha_hora', 'contenido', 'autor']

class Inicio(forms.Form):
	Nombre = forms.CharField(label = 'Nombres ', max_length = 80)

