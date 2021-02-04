""" Modulo para criar usuários """
from rest_framework import generics
from rest_framework.response import Response
from account.serializer import RegisterSerializer, UserSerializer


class RegisterApi(generics.GenericAPIView):
    """ Classe para criar o usuário e registralo na database """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """ Realização a criação do usuário """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Usuário criado com sucesso, não se esqueça de buscar seu token",
        })
