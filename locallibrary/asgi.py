"""
Módulo responsável por carregar a aplicação junto
com as configurações padrões
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

application = get_asgi_application()
