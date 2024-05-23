from django.shortcuts import render,redirect
from .models import Order, Checkout
from products.models import Product
# Create your views here.


def shoping_cart(request):
    
    if request.user.is_authenticated :
        order = Order.objects.all()
        total = sum(item.quantity*item.order.price for item in order) 
        return render(request,"orders/shoping_cart.html", {'order':order,'total':total})
        
    else :
        redirect("products:home")
        
        
def add_to_cart(request,slug):
    
    if request.user.is_authenticated :
        
        order= Product.objects.get(slug=slug)
        user,created = Order.objects.get_or_create(order= order, user=request.user)
        
        if request.method == 'GET':     
            quantity = int(request.GET.get('qty'))
            user.quantity += quantity
            user.save()

        return redirect("products:product_detail", slug=slug)
    else :
        redirect("products:home")
        
              
def remove_from_cart(request,id):
    if request.user.is_authenticated :
        order =Order.objects.get(id=id) 
        order.delete()
        return redirect("orders:shoping_cart")
        
    else :
        redirect("products:home")
   
def checkout(request):
    
    if request.method == 'POST' and 'btn_place_order' in request.POST:
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        order_note = request.POST.get('order_note')
        paypal = False
        check_payment = False
        if request.POST.get('paypal'):
            paypal = True
        if request.POST.get('check_payment') :
            check_payment = True
            
        if full_name and phone_number and address1 and city and zip and (paypal or check_payment) :
            costmer,created = Checkout.objects.get_or_create(user=request.user,
                                                             full_name= full_name,
                                                             phone_number= phone_number,
                                                             address1= address1,
                                                             address2= address2,
                                                             city= city,
                                                             zip= zip,
                                                             order_note= order_note,
                                                             paypal = paypal,
                                                             check_payment = check_payment,
                                                            
                                                       
                                                             
                                                           )
    order = Order.objects.all()
    total = sum(item.quantity*item.order.price for item in order) 
    return render(request,"orders/checkout.html",{'orders':order,'total':total})