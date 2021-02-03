from django.urls import include, path
from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getcpfs/', views.get_cpfs),
    path('addcpf/', views.add_cpf),
    path('changecpf/<str:cpf_id>/', views.change_cpf),
    path('deletecpf/<str:cpf_id>/', views.delete_cpf),
    path('checkcpf/<str:cpf_id>/', views.check_cpf),
]
