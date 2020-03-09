from django.db import models
from .classe_viagem import ClasseViagem

class Passagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()
    data_pesquisa = models.DateField()
    classe_viagem = models.TextField(choices=ClasseViagem.choices,max_length=15, default=0)
    informacoes = models.TextField(max_length=200, blank=True)