from django.contrib import admin
from backend.models import (
    Category, Product, Cart, Order,ProductCart,ProductOrder)
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(ProductCart)