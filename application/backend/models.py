from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

    class Meta:
         verbose_name_plural = 'Categories'

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    category_id = models.ManyToManyField(Category,blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_cart_id = models.ManyToManyField('ProductCart',blank=True)

    def __str__(self):
        user = User.objects.get(id=self.user_id.id).username
        return  ' '.join([str(self.id),user,'cart'])

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user_id=instance)


class ProductCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

    def __str__(self):
        cart = str(Cart.objects.get(id=self.cart_id.id))
        product = Product.objects.get(id=self.product_id.id).name
        return ' '.join([cart,product])


class Order(models.Model):
    INPROGRESS = 'IP'
    CANCELED = 'СD'
    ISDONE = 'ID'
    ORDER_STATUS = {
        INPROGRESS: 'in progress',
        CANCELED: 'canceled',
        ISDONE: 'is done',
    }
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_order_id = models.ManyToManyField('ProductOrder',blank=True)
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS,
        default=INPROGRESS,
    )

    def __str__(self):
        user = User.objects.get(id=self.user_id.id).username
        return ' '.join([str(self.id),user,'order'])


class ProductOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

    def __str__(self):
        order = str(Order.objects.get(id=self.order_id.id))
        product = Product.objects.get(id=self.product_id.id).name
        return ' '.join([order,product])