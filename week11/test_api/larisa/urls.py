
from django.urls import path
from larisa.views import category_list, category_detail

urlpatterns = [
    path('categories', category_list),
    path('category/<int:pk>', category_detail)
]