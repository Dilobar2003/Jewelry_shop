from django.db import models
from users.models import UserModel
from products.models import ProductModel

class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='order')
    products = models.ManyToManyField(ProductModel)
    total_price = models.FloatField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    adress_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.PositiveIntegerField()
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

