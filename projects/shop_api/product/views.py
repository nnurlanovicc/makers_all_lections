from rest_framework import viewsets, filters, generics
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductDetailSerializer,ProductListSerializer, ProductImageSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from review.serializers import LikeSerializer, DisLikeSerializer
from review.models import Like, DisLike, Favorite
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update','partial_update','destroy','create'):
            permissions = [IsAuthenticated]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

class CategoryView( PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]

    # def get_permissions(self):
    #     print(self.request.user)
    #     if self.action == 'create':
    #         self.permission_classes = [IsAuthenticated]
    #     return super().get_permissions()


class ProductView(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category', 'in_stock']
    search_fields = ['title','price']



    @method_decorator(cache_page(60*5))
    def list(self,request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


    @method_decorator(cache_page(60*0.75))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)




    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return self.serializer_class



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
        



class ProductImageView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]

























































    # @action(methods=['POST'], detail=True,permission_classes=[IsAuthenticated])
    # def favorite(self, request, pk=None):
    #     product = self.get_object()
    #     user = request.user
    #     serializer = FavoriteSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         try:
    #             favorite = Favorite.objects.get(product=product, author=user)
    #             favorite.delete()
    #             message = 'Избранное удалено'
    #         except Favorite.DoesNotExist:
    #             Favorite.objects.create(product=product, author=user)
    #             message = 'Добавленно в избранное'
    #         return Response(message, status=200)




# class ListFavoriteProductView(PermissionMixin, viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = ListFavoriteProductSerializer


#     @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
#     def list_favorite(self, request, pk=None):
#         favorites = Favorite.objects.all()
#         serializer = ListFavoriteProductSerializer(favorites, many=True)
#         return Response(serializer.data, status=200)





# class ProductFilteredListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['category', 'in_stock']










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