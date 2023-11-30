from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import TextoImagenes, TecnologíasYHerramientas, TecnologíasYHerramientasBN, Correo

# Create your views here.

class Inicio(ListView):
    model = TecnologíasYHerramientas
    template_name = "base/Inicio.html"
    context_object_name = "objeto_inicio"
    

class Servicios(ListView):
    model = TecnologíasYHerramientasBN
    template_name = "base/Servicios.html"
    context_object_name = "objeto_servicios"

class QuinesSomos(ListView):
    model = TextoImagenes
    template_name = "base/Quienes_somos.html"

class Contactos(CreateView):
    model = Correo
    fields = ["nombre", "email", "mensaje"]
    template_name = "base/Contactos.html"
    context_object_name = "objeto_correo"
    success_url = reverse_lazy("Contactos")
