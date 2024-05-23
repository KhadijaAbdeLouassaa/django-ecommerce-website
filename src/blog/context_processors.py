from .models import Blog 


def category_length(requast):
    category_beauty = Blog.objects.filter(category='Beauty')
    category_food = Blog.objects.filter(category='Food')
    category_lifestyle= Blog.objects.filter(category='Life Style')
    category_travel = Blog.objects.filter(category='Travel')
    
    
    return {'beauty_length':len(category_beauty),'food_length':len(category_food),'lifestyle_length':len(category_lifestyle),'travel_length':len(category_travel),}
        
        
   