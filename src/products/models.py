from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


#CATEGORY = [('Vegetables','Vegetables'), ('Fruits','Fruits'), ('Meats','Meats'),('Fastfood','Fastfood'),('Juice','Juice')]

class Categories(models.Model):
    name = models.CharField(max_length= 40)
        
    def __str__(self):
        return self.name
        
        
class Product(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    price = models.PositiveIntegerField(default= 0)
    discount = models.PositiveIntegerField(default= 0, null=True)
    category = models.ForeignKey(Categories,related_name='category', on_delete= models.CASCADE)
    added_at = models.DateField(auto_now = True)
    slug = models.SlugField(null= True,blank= True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Product,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title
        

        
class ProductReview(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    reviews = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.user} -> {self.product.title}'