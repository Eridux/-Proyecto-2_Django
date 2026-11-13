from django.db import models

# Create your models here.
class Backend(models.Model):
    tema = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=255)
    images = models.CharField(max_length=100)
    class Meta:
        db_table = 'backend'