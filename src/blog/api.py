from .serializers import BlogSirializer,CommentSirializer
from .models import Blog,Comment
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser




class BlogApi(generics.ListCreateAPIView):
    permissions_classes = [IsAuthenticated,IsAdminUser]
    queryset = Blog.objects.all()
    serializer_class = BlogSirializer
    
    
    
class SingleBlogApi(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated,IsAdminUser]
    queryset = Blog.objects.all()
    serializer_class = BlogSirializer
    
    
class BlogCommnetApi(generics.ListCreateAPIView):
    permissions_classes = [IsAuthenticated,IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSirializer
    
    
