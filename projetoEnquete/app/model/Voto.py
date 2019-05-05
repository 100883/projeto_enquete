from django.db import models
from .Usuario import Usuario
from .Empreendimento import Empreedimento

class Voto(models.Model):
    EMPR_1 = 'le jardin'
    EMPR_2 = 'evian'
    EMPR_3 = 'olimpia thermas'

    EMPR_CHOICES = (
        (EMPR_1, "Le Jardin"),
        (EMPR_2, "Evian"),
        (EMPR_3, "Olimpia Thermas"),
    )

    voto_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    voto_empr = models.ForeignKey(Empreedimento, on_delete=models.CASCADE)
    nome_empr = models.CharField(max_length=20, choices=EMPR_CHOICES)

    def __unicode__(self):
        return self.nome_empr