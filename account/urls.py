""" Modulo para adicionar o sistema de registro """
from django.urls import path
from .api import RegisterApi


urlpatterns = [
      path('register', RegisterApi.as_view(), name='api-auth'),
]
