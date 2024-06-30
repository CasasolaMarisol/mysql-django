from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

def ver_personas(request):
    personas = Persona.objects.all()
    return render(request, 'ver_personas.html', {'personas': personas})

def agregar_persona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_personas')
    else:
        form = PersonaForm()
    return render(request, 'agregar_persona.html', {'form': form})

def editar_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('ver_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'editar_persona.html', {'form': form})

def eliminar_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        persona.delete()
        return redirect('ver_personas')
    return render(request, 'eliminar_persona.html', {'persona': persona})
