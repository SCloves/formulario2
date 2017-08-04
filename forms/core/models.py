from django.db import models

# Create your models here.
class Formulario(models.Model):
	nome = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	telefone = models.CharField(max_length=13)
