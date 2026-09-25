from django.conf import settings
from django.db import models


class Remedio(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='remedios',
    )
    nome = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=0)
    horario = models.TimeField(null=True, blank=True)
    observacoes = models.CharField(max_length=500, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


#  Estoque e Alertas do Medicamento
class EstoqueRemedio(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='estoques',
    )
    nome_remedio = models.CharField(max_length=100)
    quantidade_atual = models.IntegerField()
    data_validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome_remedio} - Restam: {self.quantidade_atual}'


#  Sintomas e Efeitos Colaterais
class RegistroSintoma(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sintomas',
    )
    sintoma = models.CharField(max_length=100)
    intensidade = models.CharField(
        max_length=100, blank=True, null=True
    )
    data_ocorrencia = models.DateTimeField()
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.sintoma} ({self.intensidade})'

    

#  Consultas e Exames Agendados
class ConsultaMedica(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='consultas',
    )
    titulo_exame_consulta = models.CharField(max_length=150)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.titulo_exame_consulta} - {self.data_hora.strftime("%d/%m/%Y")}'


# Aferição de Sinais Vitais (Pressão, Glicemia, Peso, etc.)
class SinalVital(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sinais_vitais',
    )
    tipo = models.CharField(
        max_length=50
    )  # Ex: Pressão Arterial, Glicemia, Peso
    valor = models.CharField(max_length=50)  # Ex: 12x8, 98 mg/dL
    data_afericao = models.DateTimeField()

    def __str__(self):
        return f'{self.tipo}: {self.valor}'