from django.db import models

# Create your models here.
class Indumentaria(models.Model):
     title = models.CharField(max_length=20, verbose_name='titulo')
     description = models.TextField(verbose_name='descripción')
     image = models.ImageField(verbose_name='imagen', upload_to='project')
     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
     created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
     updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')
     
     # esta definicion devolver al nombre del proyecto como titulo y no como objeto
     def __str__(self) -> str:
          return self.title
     
     
     class Meta:
         verbose_name = 'indumentaria'
         verbose_name_plural = 'indumentarias'
         ordering = ['created'] # el menos en el created significa que ordenara de forma descendente si no tiene lo considera ascendente  