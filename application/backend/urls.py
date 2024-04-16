from django.urls import path
from django.urls import include
from backend.views import (
    ProductsAPIView, ProductAPIView,CartAPIView,OrderAPIView)

urlpatterns = [

    path('products',ProductsAPIView.as_view()),
    path('product',ProductAPIView.as_view()),
    path('cart',CartAPIView.as_view()),
    path('order',OrderAPIView.as_view()),
]