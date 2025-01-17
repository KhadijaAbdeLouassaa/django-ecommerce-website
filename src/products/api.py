from .serializers import CategoriesSerializers,ProductSerializers, ProductReviewSerializers
from .models import Categories,Product,ProductReview
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# --------------------------

# GET & POST Using generic  
class CategoriesListApi(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    
    
# GET & PUT & DELETE Using generic 
class SingleCategoriesApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers


# GET & POST Using generic         
class ProductListApi(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    

# GET & PUT & DELETE Using generic        
class SingleProductApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
# GET & POST Using generic     
class ProductReviewListApi(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializers
    
  

  
   
