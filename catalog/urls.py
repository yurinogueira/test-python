""" Módulo responsável por ligar as rotas """
from django.urls import include, path
from django.views.decorators.cache import cache_page
from rest_framework import routers
from catalog import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls), name='base'),
    path('getcpfs/', cache_page(60)(views.get_cpfs), name='getcpfs'),
    path('addcpf/<str:cpf_id>/', views.add_cpf, name='addcpf'),
    path('deletecpf/<str:cpf_id>/', views.delete_cpf, name='deletecpf'),
    path('checkcpf/<str:cpf_id>/', cache_page(30)(views.check_cpf), name='checkcpf'),
]
