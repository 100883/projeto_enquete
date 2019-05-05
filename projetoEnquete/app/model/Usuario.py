from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )

    nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True)
    senha = models.CharField(max_length=20)
    confirma_senha = models.CharField(max_length=20)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=14, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    profissao = models.CharField(max_length=20)
    fone = models.CharField(max_length=20)

    if senha != confirma_senha:
        msg = "As senhas são estão iguais."

    def __str__(self):
        return self.nome