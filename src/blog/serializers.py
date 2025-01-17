from .models import Blog,Comment
from rest_framework import serializers



class BlogSirializer(serializers.ModelSerializer):
    class Meta :
        model = Blog
        fields = '__all__'
        
        
        
class CommentSirializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = '__all__'