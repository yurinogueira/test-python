from django.db import models
from cpf_field.models import CPFField


class CPFModel(models.Model):

    cpf = CPFField('Informe o CPF')

    def __str__(self):
        return self.cpf
