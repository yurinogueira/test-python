from rest_framework import serializers
from catalog.models import CPFModel


class CPFSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPFModel
        fields = ['cpf']
