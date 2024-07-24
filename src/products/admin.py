from django.contrib import admin
from .models import Categories,Product,ProductReview
# Register your models here.


@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price' ,'discount' , 'category','added_at', 'image', 'slug']
    
    
    
@admin.register(ProductReview)
class ProductReviewsModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']