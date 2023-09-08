from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from review.serializers import LikeSerializer, DisLikeSerializer, FavoriteSerializer
from review.models import Like, DisLike, Favorite
from rest_framework.response import Response




class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update','partial_update','destroy','create'):
            permissions = [IsAuthenticated]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

class CategoryView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['POST'], detail=True,permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(product=product, author=user)
                like.delete()
                message = 'unlike'
            except Like.DoesNotExist:
                Like.objects.create(product=product, author=user)
                message = 'liked'
            return Response(message, status=201)
        

    @action(methods=['POST'], detail=True,permission_classes=[IsAuthenticated])
    def dislike(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = DisLikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = DisLike.objects.get(product=product, author=user)
                like.delete()
                message = 'undislike'
            except DisLike.DoesNotExist:
                DisLike.objects.create(product=product, author=user)
                message = 'disliked'
            return Response(message, status=201)
        

    @action(methods=['POST'], detail=True,permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                favorite = Favorite.objects.get(product=product, author=user)
                favorite.delete()
                message = 'Избранное удалено'
            except Favorite.DoesNotExist:
                Favorite.objects.create(product=product, author=user)
                message = 'Добавленно в избранное'
            return Response(message, status=200)


    @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
    def list_favorite(self, request, pk=None):
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=200)



    # @action(methods=['POST', 'GET'], detail=True,permission_classes = [IsAuthenticated])
    # def favorite(self, request, pk=None):
    #     product = self.get_object()
    #     user = request.user

    #     if request.method == 'GET':
    #         list_favorite = Favorite.objects.all()
    #         serializer = FavoriteSerializer(list_favorite, many=True)
    #         return Response(serializer.data, status=200)
    #     elif request.method == 'POST':
    #         serializer = FavoriteSerializer(data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             try:
    #                 favorite = Favorite.objects.get(product=product, author=user)
    #                 favorite.delete()
    #                 message = 'Избранное удалено'
    #             except Favorite.DoesNotExist:
    #                 Favorite.objects.create(product=product, author=user)
    #                 message = 'Добавленно в избранное'
    #             return Response(message, status=200)