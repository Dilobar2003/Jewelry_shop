from django.db import models

from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/', null=True, blank=True)
   

class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True )
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    adress = models.CharField(max_length=200, null=True, blank=True)
    adress_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    zip_code = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}"




    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
   
