from django.db import models
from django.utils.text import slugify
# Create your models here.


CATEGORY = [('Vegetables','Vegetables'), ('Fruits','Fruits'), ('Meats','Meats'),('Fastfood','Fastfood'),('Juice','Juice')]

class Product(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    price = models.PositiveIntegerField(default= 0)
    category = models.CharField(max_length= 25,choices = CATEGORY)
    added_at = models.DateField(auto_now = True)
    slug = models.SlugField(null= True,blank= True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Product,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title