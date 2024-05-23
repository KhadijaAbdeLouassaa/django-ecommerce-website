from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

CATEGORY = [('Food','Food'),('Beauty','Beauty'),('Life Style','Life Style'),('Travel','Travel')]

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images")
    created_at = models.DateField(auto_now=True)
    category =  models.CharField(max_length=15, choices=CATEGORY)
    slug = models.SlugField(null= True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    commenter = models.ForeignKey(User,on_delete= models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    