from django.db import models

class Empreedimento(models.Model):
    EMPR_1 = 'le jardin'
    EMPR_2 = 'evian'
    EMPR_3 = 'olimpia thermas'

    EMPR_CHOICES = (
        (EMPR_1, "Le Jardin"),
        (EMPR_2, "Evian"),
        (EMPR_3, "Olimpia Thermas"),
    )

    descricao = models.CharField(max_length=20, choices=EMPR_CHOICES)
    foto_capa = models.ImageField(upload_to="images")

    def __str__(self):
        return self.descricao