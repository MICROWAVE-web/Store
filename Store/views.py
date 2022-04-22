from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer_for_queryset = ProductSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class CategoryView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer_for_queryset = CategorySerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class ProductViewById(APIView):
    def get(self, request, product_id):
        queryset = Product.objects.get(id=product_id)
        serializer_for_queryset = ProductByIdSerializer(
            instance=queryset
        )
        return Response(serializer_for_queryset.data)


class CategoryViewById(APIView):
    def get(self, request, category_id):
        queryset = Category.objects.get(id=category_id)
        serializer_for_queryset = CategoryByIdSerializer(
            instance=queryset
        )
        return Response(serializer_for_queryset.data)
