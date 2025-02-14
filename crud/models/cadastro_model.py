from django.db import models

class CadastroModel(models.Model):
    documento = models.CharField(max_length=14, null=True, blank=True)
    nome = models.CharField(max_length=100 , null=True , blank=True)
    endereco = models.CharField(max_length=100, null=True , blank=True)

    def __str__(self):
        return self.nome if self.nome else "Sem Nome"