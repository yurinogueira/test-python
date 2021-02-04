""" Modulo para serialização """
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """ Converte o objeto do usuário em um json """
    class Meta:
        """ Define quais campos serão convertidos """
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Função para criar um usuário
        :param validated_data: nome do usuário com uma validação
        :return: objeto do usuário
        """
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        first_name=validated_data['email'])
        return user


class UserSerializer(serializers.ModelSerializer):
    """ Uma classe simples para converter o objeto user """
    class Meta:
        """ Pega todos os campos do User """
        model = User
        fields = '__all__'
