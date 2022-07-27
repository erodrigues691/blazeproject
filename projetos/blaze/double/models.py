import email
from pyexpat import model
from statistics import mode
from django.db import models

class Double(models.Model):
    nome = models.CharField(max_length=256)
    data_nascimento = models.DateTimeField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self) -> str():
        return self.nome

class Contato(models.Model):
    nome= models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    double = models.ForeignKey(Double, on_delete=models.CASCADE)

    def __str__(self) -> str:   
        return  self.nome
