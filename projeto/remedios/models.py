from django.db import models

# Create your models here.

class Remedio(models.Model):
    nome = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50) 
    quantidade = models.IntegerField(default=0)
    horario = models.TimeField(null=True, blank=True)
    observacoes = models.CharField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

 