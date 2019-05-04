from django.db import models
from .Usuario import Usuario

class Empreedimento(models.Model):
    descricao = models.CharField(max_length=200)
    foto_capa = models.ImageField(upload_to="images")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao