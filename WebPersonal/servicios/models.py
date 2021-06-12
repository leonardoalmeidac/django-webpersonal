from django.db import models

# Create your models here.
# Se hereda de models.Model (solo cuando se desea mapear una tabla de una BD)

class Service(models.Model) :
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name="Imagen") #upload_to="servicios")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de actualización")

    class Meta :
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title