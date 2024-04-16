from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(default=0)
    name = serializers.CharField(max_length=150)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(default=0)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=300)
    category_id = CategorySerializer(read_only=True, many=True)
    price = serializers.IntegerField(default=0)

class ProductCartSerializer(serializers.Serializer):
    id = serializers.IntegerField(default=0)
    cart_id = serializers.CharField()
    product_id = ProductSerializer(read_only=True)
    amount = serializers.IntegerField(default=1)
    

class ProductOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(default=0)
    order_id = serializers.CharField()
    product_id = ProductSerializer(read_only=True)
    amount = serializers.IntegerField(default=1)

class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = UserSerializer(read_only=True)
    product_cart_id = ProductCartSerializer(read_only=True, many=True)

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = UserSerializer(read_only=True)
    product_order_id = ProductOrderSerializer(read_only=True, many=True)
    status = serializers.CharField()