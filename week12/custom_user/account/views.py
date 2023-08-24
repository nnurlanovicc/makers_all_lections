from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, ForgotPasswordCompleteSerializer,ForgotPasswordSerializer, ChangePasswordSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permissions import IsActivePermission
from rest_framework.permissions import IsAuthenticated



User = get_user_model()


class RegistrationView(APIView):

    def post(self,request):
        serializer = RegistrationSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Аккаунт успешно создан', status=201)
    

    # def get(self,request):
    #     queryset = User.objects.all()
    #     serializer = RegistrationSerializer(queryset, many=True)
    #     return Response(serializer.data, status=200)
    

class ActivationView(APIView):
    def post(self,request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('аккаунт успешно активирован', status=200)
        return Response('иди на хуй')
    

class loginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):

    permission_classes = [IsActivePermission]

    def post(selfself, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('иди на три веселые буквы')

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'пароль успешно обновлен'
            )


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(
            data = request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response(
                'Вам выслали сообщение для восстановления'
            )


class ForgotPasswordCompleteView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(
            data=request.data)
        if serializer.is_valid(
                raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Пароль успешно изменен'
            )