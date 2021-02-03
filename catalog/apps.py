"""
Esse módulo serve para definir qual será as
aplicações rodadas neste servidor
"""
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """ Configura a aplicação root """
    name = 'catalog'
