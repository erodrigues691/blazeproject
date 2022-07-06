from pyexpat import model
from statistics import mode
from django.db import models

class Double(models.Model):
    nome = models.CharField(max_length=256)
    datanascimento = models.DateTimeField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

