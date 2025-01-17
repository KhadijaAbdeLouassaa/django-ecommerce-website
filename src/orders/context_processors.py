from orders.models import Order
# add your context processor function here
# len of item that your want to show in all html templates 
# don't forget to add the path to settings.py !


# this is for cart icon   
def order_length(request):
    if request.user.is_authenticated :
        try : 
            items = Order.objects.filter(user=request.user)
            return {'order_length':len(items)}
           
        except Order.DoesNotExist :
            pass
    # default value   
    return {'order_length':0}