from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento', 'domicilio', 'telefono', 'correo')
