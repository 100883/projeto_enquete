from django.db import models
from .Usuario import Usuario
from .Empreendimento import Empreedimento

class Voto(models.Model):
    voto_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    voto_empr = models.ForeignKey(Empreedimento, on_delete=models.CASCADE)

    def __str__(self):
        return self.voto_empr