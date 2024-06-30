from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'fecha_nacimiento', 'domicilio', 'telefono', 'correo']
