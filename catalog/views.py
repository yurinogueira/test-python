"""
Módulo responsável por executar todos os
métodos CRUD e de verificação
"""
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.decorators import renderer_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from catalog.models import CPFModel
from catalog.serializers import CPFSerializer


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_cpfs(request):
    """
    Carrega e retorna a lista de CPFs bloqueados em formato json
    :param request: Requerente da função
    :return: JsonResponse com a lista de CPFs.
    """
    cpf = CPFModel.objects.all()
    try:
        serializer = CPFSerializer(cpf, many=True)
        return JsonResponse({'cpfs': serializer.data},
                            safe=False,
                            status=status.HTTP_200_OK)

    except ConnectionError:
        return JsonResponse({'erro': 'Problema de conexão interno.'},
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_cpf(request, cpf_id):
    """
    Recebe um CPF em formato json insere no banco de dados
    :param cpf_id: CPF em string
    :param request: Requerente da função
    :return: Resposta da inserção
    """
    try:
        cpf = CPFModel.objects.create(cpf=cpf_id)
        serializer = CPFSerializer(cpf)
        return JsonResponse({'cpf': serializer.data},
                            safe=False,
                            status=status.HTTP_201_CREATED)

    except ObjectDoesNotExist as object_exception:
        return JsonResponse({'erro': str(object_exception)},
                            safe=False,
                            status=status.HTTP_204_NO_CONTENT)

    except ConnectionError:
        return JsonResponse({'erro': 'Algo deu errado.'},
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_cpf(request, cpf_id):
    """
    Remove um CPF do banco de dados utilizando json
    :param request: Requerente da função
    :param cpf_id: CPF em string
    :return: resposta da remoção
    """
    try:
        cpf_object = CPFModel.objects.get(cpf=cpf_id)
        cpf_object.delete()
        return Response(status=status.HTTP_200_OK)

    except ObjectDoesNotExist as object_exception:
        return JsonResponse({'erro': str(object_exception)},
                            safe=False,
                            status=status.HTTP_204_NO_CONTENT)

    except ConnectionError:
        return JsonResponse({'erro': 'Algo deu errado.'},
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def check_cpf(request, cpf_id):
    """
    Verifica se o CPF informado é ou não permitido
    :param request: Requerente da função
    :param cpf_id: CPF em string
    :return: 'DENY' caso o CPF esteja no banco de dados,
    'ALLOW' caso contrário
    """
    try:
        cpf_object = CPFModel.objects.get(cpf=cpf_id)
        serializer = CPFSerializer(cpf_object)
        return Response({'result': 'DENY'},
                        template_name='deny.html',
                        status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response({'result': 'ALLOW'},
                        template_name='allow.html',
                        status=status.HTTP_200_OK)

    except ConnectionError:
        return JsonResponse({'erro': 'Algo deu errado.'},
                            safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
