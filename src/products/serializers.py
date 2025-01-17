from rest_framework import serializers
from .models import Categories,Product,ProductReview

# --> serializers class

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta :
        model = Categories
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta :    
        model = Product
        fields = '__all__'
      
      
      
class ProductReviewSerializers(serializers.ModelSerializer):
    class Meta :    
        model = ProductReview
        fields = '__all__'
      