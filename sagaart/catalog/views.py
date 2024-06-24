from rest_framework import viewsets

from catalog.models import Category, Product
from catalog.serializers import (
    CategorySerializer, ProductSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
