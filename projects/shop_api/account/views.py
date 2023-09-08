from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



User = get_user_model()



class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer()) # для отображения параметров POST запроса в docs
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response('вы успешно зарегались', status=201)
    
class ActivationView(APIView):
    def get(self,request, email, activation_code):
        user = User.objects.filter(email=email,activation_code=activation_code).first()
        if not user:
            return Response('пользователь не найден')
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('аккаунт активирован', status=200)



