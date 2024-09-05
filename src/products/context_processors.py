from accounts.models import UserProfile
from .models import Categories
# add your context processor function here
# len of item that your want to show in all html templates 
# don't forget to add the path to settings.py !

# this is for favourite icon
def item_length(request):
    if request.user.is_authenticated :
        try :
            user = UserProfile.objects.get(user = request.user)
            items = user.favorite_products.all()
            return {'item_length':len(items)}
           
        except UserProfile.DoesNotExist :
            pass
    # default value   
    return {'item_length':0}
    
def category(request):
    categories = Categories.objects.all()

    return {'categories':categories}