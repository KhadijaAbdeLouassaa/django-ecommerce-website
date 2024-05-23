from django.contrib import admin
from .models import Blog,Comment
# Register your models here.


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'image']
    
    
@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['post', 'commenter', 'created_at']