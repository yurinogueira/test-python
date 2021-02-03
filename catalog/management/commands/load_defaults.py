from django.core.management.base import BaseCommand, CommandError

from catalog.models import CPFModel


class Command(BaseCommand):
    help = 'Carrega uma lista pré-definida de CPFs'

    def handle(self, **options):
        self.stdout.write('Carregando lista pré-definida de CPFs')
        arq = open('deny.txt', 'r')
        for linha in arq:
            cpf_name = linha.replace('\n', '')
            CPFModel.objects.create(cpf=cpf_name)
        arq.close()
