""" Módulo responsável por ligar as rotas """
from django.urls import include, path
from django.views.decorators.cache import cache_page
from rest_framework import routers
from catalog import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getcpfs/', cache_page(60)(views.get_cpfs)),
    path('addcpf/', views.add_cpf),
    path('changecpf/<str:cpf_id>/', views.change_cpf),
    path('deletecpf/<str:cpf_id>/', views.delete_cpf),
    path('checkcpf/<str:cpf_id>/', cache_page(30)(views.check_cpf)),
]
