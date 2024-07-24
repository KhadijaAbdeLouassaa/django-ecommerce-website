from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    favorite_products = models.ManyToManyField(Product,null=True, blank=True)
    def __str__(self):
        return self.user.username
        
        
    

def create_user_profile(sender,**kargs):
    if kargs['created'] :
        UserProfile.objects.create(user=kargs['instance'])
        
# when you create User run create_user_profile function to create profle        
post_save.connect(create_user_profile,sender=User)