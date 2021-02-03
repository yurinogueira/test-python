from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.utils import json

from catalog.models import CPFModel
from catalog.serializers import CPFSerializer


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_cpfs(request):
    cpf = CPFModel.objects.all()
    serializer = CPFSerializer(cpf, many=True)
    return JsonResponse({'cpfs': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_cpf(request):
    payload = json.loads(request.body)
    try:
        cpf = CPFModel.objects.create(cpf=payload["cpf"])
        serializer = CPFSerializer(cpf)
        return JsonResponse({'cpfs': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'erro': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'erro': 'Algo deu errado.'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def change_cpf(request, cpf_id):
    payload = json.loads(request.body)
    try:
        cpf_data = CPFModel.objects.filter(cpf=cpf_id)
        cpf_data.update(**payload)
        cpf_object = CPFModel.objects.get(cpf=cpf_id)
        serializer = CPFSerializer(cpf_object)
        return JsonResponse({'cpf': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'erro': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'erro': 'Algo deu errado.'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_cpf(request, cpf_id):
    try:
        cpf_object = CPFModel.objects.get(cpf=cpf_id)
        cpf_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'erro': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'erro': 'Algo deu errado.'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def check_cpf(request, cpf_id):
    try:
        cpf_object = CPFModel.objects.get(cpf=cpf_id)
        serializer = CPFSerializer(cpf_object)
        return Response({'cpf': serializer.data}, template_name='deny.html', status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'cpf': 'não existe'}, template_name='allow.html', status=status.HTTP_200_OK)
    except Exception:
        return JsonResponse({'erro': 'Algo deu errado.'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
