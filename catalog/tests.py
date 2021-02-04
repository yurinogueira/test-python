""" Modulo de tests """
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from catalog.models import CPFModel


class Tests(APITestCase):
    """ Classe responsável pela execução dos tests """

    def setUp(self):
        """
        Define um usuário padrão para os testes
        e carrega as urls
        :return:
        """
        self.user = User.objects.create_superuser(username='testename',
                                                  email='emailteste@teste.com',
                                                  password='testando')
        self.client = Client()
        self.api_auth_url = reverse('api-auth')
        self.jwt_url = reverse('get_token')

        cpf_allow_object = CPFModel(cpf='561.412.413-60')
        cpf_allow_object.save()

        cpf_delete_object = CPFModel(cpf='757.617.201-08')
        cpf_delete_object.save()

    def test_wrong_password_to_get_token(self):
        """
        Informa a senha errada para verificar
        e espera o retorno de um erro
        """
        data = {
            'username': self.user.username,
            'password': 'senhaerrada',
        }
        response = self.client.post(self.jwt_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_right_password_to_get_token(self):
        """
        Informa a senha certa para verificar
        e espera o retorno de uma confirmação
        """
        data = {
            'username': self.user.username,
            'password': 'testando',
        }
        response = self.client.post(self.jwt_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_cpf(self):
        """
        Carrega o JWT token do cliente e
        adiciona um CPF na lista e
        retorna se foi criado
        """
        data = {
            'username': self.user.username,
            'password': 'testando',
        }
        response = self.client.post(self.jwt_url, data)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data['token'])

        add_response = client.post('http://localhost:8000/catalog/addcpf/564.408.543-05/')
        self.assertEqual(add_response.status_code, status.HTTP_201_CREATED)

    def test_check_cpf_allow(self):
        """
        Verifica se o CPF informado
        está permitido e retorna
        ALLOW
        """
        client = APIClient()

        get_response = client.get('http://localhost:8000/catalog/checkcpf/564.408.543-05/')
        self.assertEqual('ALLOW', get_response.data['result'])

    def test_check_cpf_deny(self):
        """
        Verifica se o CPF informado
        está bloqueado e retorna
        DENY
        """
        client = APIClient()

        get_response = client.get('http://localhost:8000/catalog/checkcpf/561.412.413-60/')
        self.assertEqual('DENY', get_response.data['result'])

    def test_delete_cpf(self):
        """
        Carrega o JWT token do cliente e
        delete um CPF da lista
        retornando a confirmação
        """
        data = {
            'username': self.user.username,
            'password': 'testando',
        }
        response = self.client.post(self.jwt_url, data)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data['token'])

        add_response = client.delete('http://localhost:8000/catalog/deletecpf/757.617.201-08/')
        self.assertEqual(add_response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Carrega o JWT token do cliente e
        cria um usuário novo, gera seu
        token e retorna a confirmação
        """
        data = {
            'username': self.user.username,
            'password': 'testando',
        }
        response = self.client.post(self.jwt_url, data)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data['token'])

        new_user_data = {
            'username': 'novousuario',
            'password': 'senhadele',
            'email': 'emaildele@teste.com'
        }

        new_user_response = client.post(self.api_auth_url, new_user_data)
        self.assertEqual(new_user_response.status_code, status.HTTP_200_OK)

        confirmation_data = {
            'username': 'novousuario',
            'password': 'senhadele',
        }
        token_response = self.client.post(self.jwt_url, confirmation_data)
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
