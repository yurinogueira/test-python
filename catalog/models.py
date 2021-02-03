"""
Esse módulo serve para criar os módelos disponíveis
para ser salvos no banco de dados
"""
from django.db import models
from cpf_field.models import CPFField


class CPFModel(models.Model):
    """
    Objeto CPFModel com um verificador se o
    CPF é válido ou não
    """
    cpf = CPFField('Informe o CPF')

    def __str__(self):
        return self.cpf
