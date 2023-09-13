from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, ProductView, ProductImageView


router = DefaultRouter()
router.register('categories', CategoryView)
router.register('products', ProductView)
# router.register('favorites', ListFavoriteProductView)

# router.register('serch', ProductFilteredListView)

urlpatterns = [
    path('', include(router.urls)),
    path('add-product-image/', ProductImageView.as_view())
]





# urlpatterns = [
#     path('categories/', CategoryView.as_view({'get': 'list','post': 'create',})),
#     path('categories/<slug:pk>/', CategoryView.as_view({'get': 'retrieve',
#                                                         'put': 'update',
#                                                         'patch': 'partial_update',
#                                                         'delete': 'destroy'}))

# ]
