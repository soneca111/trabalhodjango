from django.conf import settings
from django.db import models

class Remedio(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='remedios'
    )
    nome = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50) 
    quantidade = models.IntegerField(default=0)
    horario = models.TimeField(null=True, blank=True)
    observacoes = models.CharField(max_length=500, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome