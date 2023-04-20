from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'description', 'created_date']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name']
