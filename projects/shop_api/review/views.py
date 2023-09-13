from django.shortcuts import render
from .models import Like, DisLike, Comment, Rating
from .serializers import CommentSerializer, RatingSerializer, FavoriteListSerializer, FavoriteCreateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAuthor
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication



class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ('update','partial_update','destroy'):
            permissions = [IsAuthor]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

class CommentView(PermissionMixin,ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingView(PermissionMixin,ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteListView(ListAPIView):
    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.request.user.favorites.all()

        

class FavoriteCreateView(CreateAPIView):
    serializer_class = FavoriteCreateSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FavoriteDeleteView(DestroyAPIView):
    lookup_url_kwarg = 'pk'
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication]


    def get_queryset(self):
        return self.request.user.favorites.all()