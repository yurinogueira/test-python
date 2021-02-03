""" Módulo responsável por serializar um objeto em formato json """
from rest_framework import serializers
from catalog.models import CPFModel


class CPFSerializer(serializers.ModelSerializer):
    """ Classe responsável para começa a serialização """
    class Meta:
        """ Formatação da serialização para o objeto CPFModel """
        model = CPFModel
        fields = ['cpf']
