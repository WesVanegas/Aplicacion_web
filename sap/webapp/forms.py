from django import forms
from personas.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model= Persona
        fields = ['nombre', 'apellido', 'email', 'edad', 'genero', 'celular']