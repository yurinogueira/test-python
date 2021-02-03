"""
Módulo responsável por registrar objetos que serão
manipulados pelo Django Admin
"""
from django.contrib import admin
from catalog.models import CPFModel

admin.site.register(CPFModel)
