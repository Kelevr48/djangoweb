from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Autor
from .models import Entrada
from .models import Figuras
from .forms import *

def welcome(request):
	autores = Autor.objects.all();
	return render(request, 'welcome.html')
	#return HttpResponse('<h1>Bienvido</h1>')

def autores(request):
	if request.method == 'POST':
		form = AutoForm(request.POST)
		if form.is_valid():
			autor = Autor()
			autor.nombres = form.cleaned_data['nombres']
			autor.apellidos = form.cleaned_data['apellidos']
			autor.save()
			return redirect('autores')
	else:
		form = AutoForm
		todosAutores = Autor.objects.all()
		return render(request, 'autores.html', {'autores':todosAutores, 'form':form})

def edit_autor(request, id):
	autor = Autor.objects.get(id_autor=id)
	form = AutoForm(instance=autor)
	if request.method == 'POST':
		form_cambiado = AutoForm(request.POST, instance=autor)
		if form_cambiado.is_valid():
			form_cambiado.save()
			return redirect('autores')
	else:
		return render(request, 'autores.html', {'form':form, 'autor': autor})

def delete_autor(request, id):
	autor = Autor.objects.get(id_autor=id)
	autor.delete()
	return redirect('autores')

def entradas(request):
	if request.method == 'POST':
		form2 = EntradaForm(request.POST)
		if form2.is_valid():
			entrada = Entrada()
			entrada.titular = form.cleaned_data['entradas.titular']
			entrada.save()
			return redirect('entradas')
	else:
		form2 = EntradaForm
		todosEntradas = Entrada.objects.all()
		return render(request, 'entradas.html', {'entradas':todosEntradas, 'form2':form2})

def index(request):
	return HttpResponse('<h1>Inicio</1> <a href="inicio">Bienvenido</a>')



def inicio(request):
	figuras = Figuras.objects.all()
	return render(request, 'inicio.html', {'range':range(1, 170)})

def registro(request):
	registro = Registro.objects.all();
	return render(request, 'registro.html')

def faltantes(request):
	faltantes = Faltantes.objects.all();
	return render(request, 'faltantes.html')


