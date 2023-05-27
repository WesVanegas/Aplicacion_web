from django.shortcuts import render, redirect
from django.http import HttpResponse

from personas.models import Persona

from .forms import PersonaForm
# Create your views here.

def index(request):
    return render(request, 'index.html')


def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'persona_list.html', {'personas':personas})


def persona_register(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista')
    else:
        form = PersonaForm()
    return render(request, 'persona_register.html', {'form':form})

def bandas(request):
    return render(request, 'bandas.html')

def galeria(request):
    return render(request, 'galeria.html')
