from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    favorite_products = models.ManyToManyField(Product)
    def __str__(self):
        return self.user.username
        
        
    