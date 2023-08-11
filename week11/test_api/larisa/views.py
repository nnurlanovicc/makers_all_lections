from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Category
from .serialisers import CategorySerializer


@api_view(['GET'])
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=200)
    except Category.DoesNotExist:
        return Response('Такой категории не существует', status=200)
    

