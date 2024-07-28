from django.db import models
from django.utils import timezone




class BrandModel(models.Model):
    name = models.CharField(max_length=50)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=50)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'





class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    short_discription = models.TextField()
    long_discription = models.TextField()
    price = models.FloatField()
    real_price = models.FloatField(default=0)
    discount = models.PositiveIntegerField(default=0)
    main_image = models.ImageField(upload_to='products/')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    size = models.ManyToManyField(ProductSizeModel, related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)



    
    def is_discount(self):
        return self.discount != 0
    

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3
    
    @staticmethod
    def get_cart_objects(cart):
        return ProductModel.objects.filter(id__in=cart)
    



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)
    


