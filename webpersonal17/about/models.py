from django.db import models

# Create your models here.
class About(models.Model):
     apellido = models.CharField(max_length=20, verbose_name='apellido')
     nombre = models.CharField(max_length=20, verbose_name='nombre')
     image = models.ImageField(verbose_name='imagen', upload_to='project')
     descripcion = models.TextField(verbose_name='descripcion')
     email = models.CharField(max_length=100, verbose_name='email', default='xxxxx@xxxxxxxx.com')
     created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
     updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')
     
     # esta definicion devolver al nombre del proyecto como titulo y no como objeto
     def __str__(self) -> str:
          return (self.apellido + ' ' +  self.nombre)
     
     
     class Meta:
         verbose_name = 'integrante'
         verbose_name_plural = 'integrantes'
         ordering = ['created'] # el menos en el created significa que ordenara de forma descendente si no tiene lo considera ascendente