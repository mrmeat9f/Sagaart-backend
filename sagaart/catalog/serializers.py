from rest_framework import serializers

from catalog.models import Category, Product
from catalog.fields import Base64ImageField


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    photo = Base64ImageField()

    class Meta:
        model = Product
        fields = '__all__'
