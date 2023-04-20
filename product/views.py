from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from user.permissions import IsOwnerOrReadOnly


class ProductListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        return qs


class CategoryListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all()
        return qs


class ProductCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = CategorySerializer


class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class CategoryUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductDetailAPIView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class CategoryDetailAPIView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class CategoryDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'






