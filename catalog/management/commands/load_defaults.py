"""
Esse módulo serve para carregar a lista pré-definida
de CPFs que está contida no arquivo deny.txt na raiz
"""
from django.core.management.base import BaseCommand
from catalog.models import CPFModel


class Command(BaseCommand):
    """
    Classe responsável por ler a lista de CPFs
    """
    help = 'Carrega uma lista pré-definida de CPFs'

    def handle(self, *args, **options):
        self.stdout.write('Carregando lista pré-definida de CPFs')
        arq = open('deny.txt', 'r')
        for line in arq:
            cpf_name = line.replace('\n', '')
            CPFModel.objects.create(cpf=cpf_name)
        arq.close()
