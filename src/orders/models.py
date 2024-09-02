from django.db import models
from django.contrib.auth.models import User
from products.models import Product 

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    order = models.ForeignKey(Product,on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now=True)
    
    def  __str__(self):
        return f"{self.user.username}______{self.order}"
        
    
  
    

class Checkout(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    full_name = models.CharField(max_length= 15)
    phone_number = models.CharField(max_length= 15)
    city = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50,blank=True,null=True)
    zip = models.CharField(max_length= 15)
    order_note = models.TextField(blank=True,null=True)
    paid = models.BooleanField(default=False)
    
    def  __str__(self):
        return self.user.username
  