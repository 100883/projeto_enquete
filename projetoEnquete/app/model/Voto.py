from django.db import models
from .Usuario import Usuario
from .Empreendimento import Empreedimento

class Voto(models.Model):
    voto_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome_empr = models.CharField(max_length=20, choices=Empreedimento.EMPR_CHOICES)

    def __str__(self):
        return self.nome_empr