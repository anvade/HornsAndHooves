from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from backend.models import (
    Product, Category,Cart,ProductCart,Order,ProductOrder)

from backend.serializer import (
    ProductSerializer, CategorySerializer, CartSerializer,
    ProductCartSerializer,ProductOrderSerializer,OrderSerializer)

from backend.permissions import IsOwner
# Create your views here.

class ProductsAPIView(APIView):
    def post(self,request):
        try:
            category_name = CategorySerializer(data =request.data)
            category_name.is_valid(raise_exception=True)
            category_set = Category.objects.filter(name = category_name.data['name'])
            category_id = CategorySerializer(category_set,many=True).data[0]['id']
            products_set = Product.objects.filter(category_id = category_id)
            return Response({'products':ProductSerializer(products_set,many=True).data})
        except:
            return Response(data={'detail':'category not found'},status=404)

class ProductAPIView(APIView):
    def get(self,request):
        try:
            product_set = Product.objects.get(id = request.GET.get('id'))
        except:
            return Response({'detail':'product dont found'})
        return Response(ProductSerializer(product_set).data)

class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        cart = Cart.objects.get(user_id = request.user)
        serializer_cart = CartSerializer(cart)
        return Response(serializer_cart.data)
    
    def post(self,request):
        try:
            request_product_id = request.data['product_id']
            request_amount = request.data['amount']
            cart = Cart.objects.get(user_id = request.user)
            product = Product.objects.get(id = request_product_id)
        except:
            return Response({'detail':'product not found'})
        product_cart = ProductCart.objects.create(
            cart_id = cart,
            product_id = product,
            amount = request_amount
        )
        cart.product_cart_id.add(product_cart)

        return Response(CartSerializer(cart).data)


    def put(self,request):
        try:
            request_id = request.data['id']
            cart = Cart.objects.get(user_id = request.user)
            request_amount = request.data['amount']
            product_cart = ProductCart.objects.get(id = request_id)
        except:
            return Response({'detail':'product not found in card'})
        
        product_cart.amount = request_amount
        product_cart.save()

        return Response(CartSerializer(cart).data)

    def delete(self,request):
        try:
            request_id = request.GET.get('id')
            product_cart = ProductCart.objects.get(id = request_id)
        except:
            return Response({'detail':'product not found in card'})
        product_cart.delete()

        return Response({'detail':'deleted successfully'})


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        cart = Cart.objects.get(user_id = request.user)
        product_cart = ProductCart.objects.filter(cart_id = cart)
        if not product_cart:
            return Response({'detail':'cart is empty'})
        order = Order.objects.create(user_id = request.user)
        for product in product_cart:
            product_order = ProductOrder.objects.create(
            order_id = order,
            product_id = product.product_id,
            amount = product.amount
            )
            order.product_order_id.add(product_order)
            product.delete()
        order.save()
        return Response(OrderSerializer(order).data)