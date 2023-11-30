from django.db import models

# Create your models here.

class TextoImagenes(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)    
    parrafo = models.TextField(max_length=10000, null=True, blank=True)
    imagenes = models.ImageField(upload_to="imagenes/", null=True, blank=True)

    def __str__(self):
        return self.titulo

class TecnologíasYHerramientas(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    imagenes = models.ImageField(upload_to="imagenes/tyh_color", null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
class TecnologíasYHerramientasBN(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    imagenes = models.ImageField(upload_to="imagenes/tyh_gris", null=True, blank=True)
    parrafo = models.TextField(max_length=10000, null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
class Servicios(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    imagenes = models.ImageField(upload_to="imagenes/servicios", null=True, blank=True)
    parrafo = models.TextField(max_length=10000, null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
class Correo(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    mensaje = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.nombre