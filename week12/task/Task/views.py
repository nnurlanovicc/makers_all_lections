# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import TaskSerializer, ProjectSerializer, CommentSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class TaskView(APIView):

#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         serializer.save()
#         return Response('Задача успешно создан', status=201)
    
# class ProjectView(APIView):

#     def post(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         serializer.save()
#         return Response('Проект успешно создан' , status=201)
    

# class CommentView(APIView):

#     def post(self, request):
#         serializer = CommentSerializer(data=request.data)
#         serializer.save()
#         return Response('Комментарии создан' , status=201)
    
