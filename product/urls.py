from django.urls import path
from product import views


urlpatterns = [
    path('all', views.ProductListAPIView.as_view(), name='all-product'),
    path('category/', views.CategoryListAPIView.as_view(), name='all-category'),
    path('create/', views.ProductCreateAPIView.as_view(), name='create-product'),
    path('category/create/', views.CategoryCreateAPIView.as_view(), name='create-category'),
    path('<int:id>/update/', views.ProductUpdateAPIView.as_view(), name='update-product'),
    path('category/<int:id>/update/', views.CategoryUpdateAPIView.as_view(), name='update-category'),
    path('<int:id>/', views.ProductDetailAPIView.as_view(), name='retrieve-product'),
    path('category/<int:id>/', views.CategoryDetailAPIView.as_view(), name='retrieve-category'),
    path('<int:id>/delete', views.ProductDeleteAPIView.as_view(), name='delete-product'),
    path('category/<int:id>/delete', views.CategoryDeleteAPIView.as_view(), name='delete-category'),
]
