from django.db import models
from products.models import ProductModel
from users.models import UserModel
from django.db import IntegrityError


class WishListModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


    @staticmethod

    def create_or_delete(user, product):
        try:
            WishListModel.objects.create(user=user, product=product)
        except IntegrityError:
            WishListModel.objects.get(user=user, product=product).delete()    




    def __str__(self):
        return f"{self.user} {self.product}"
    
    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = ['user', 'product']





class ContactMessageModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'




class BannerModel(models.Model):
    collection = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='banners')
    status = models.BooleanField(default=True)



    def __str__(self):
        return self.title
    


    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'





