from django.shortcuts import render,redirect
from .models import Order, Checkout
from products.models import Product
import stripe
from django.conf import settings
from django.urls import reverse
from decimal import Decimal
from django.contrib import messages

# Create your views here.


def shoping_cart(request):
    
    if request.user.is_authenticated :
        order = Order.objects.all()
        total = sum(item.quantity*item.order.price for item in order) 
        compon_discount = request.session.get('compon_discount')
        
        if compon_discount :
        
            initial_total = sum(item.quantity*item.order.price for item in order) 
            final_total = initial_total - (compon_discount * initial_total / 100)
            return render(request,"orders/shoping_cart.html", {'order':order,'total':final_total,'subtotal':total,'discount':compon_discount})
       
        
        
        if request.method == 'POST' and 'to_checkout_btn' in request.POST :
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            zip = request.POST.get('zip')
            order_note = request.POST.get('order_note')
            
            if full_name and phone_number and address1 and city and zip  :
                costmer,created = Checkout.objects.get_or_create(user=request.user,
                                                                 full_name= full_name,
                                                                 phone_number= phone_number,
                                                                 address1= address1,
                                                                 address2= address2,
                                                                 city= city,
                                                                 zip= zip,
                                                                 order_note= order_note,
                                                                 paid = True
                                                                )
                request.session['order'] = costmer.id
                return redirect("orders:checkout")
            else :
                messages.add_message(request,messages.ERROR, "Please fill your informations")
            
        
        return render(request,"orders/shoping_cart.html", {'order':order,'total':total,'subtotal':total,'discount':compon_discount})
           
        
        
    else :
        messages.add_message(request,messages.ERROR, "Please login ")
        return redirect("products:home")
        
        
def add_to_cart(request,slug):
    
    if request.user.is_authenticated :
        order= Product.objects.get(slug=slug)
        user,created = Order.objects.get_or_create(order= order, user=request.user)
               
        if 'qty' in request.GET and  request.GET.get('qty') != '0':            
            quantity = request.GET.get('qty')
            print(quantity)
            
            try :
                user.quantity += int(quantity)     
                user.save()
                
            except ValueError:
                user.quantity += 1               
                user.save()           
        else:      
          user.quantity += 1
          user.save()
          
        return redirect("products:product_detail", slug=slug)
    else :
        messages.add_message(request,messages.ERROR, "Please login ")
        return redirect("products:home")
        
              
def remove_from_cart(request,id):
    if request.user.is_authenticated :
        order =Order.objects.get(id=id) 
        order.delete()
        return redirect("orders:shoping_cart")
        
    else :
        messages.add_message(request,messages.ERROR, "Please login ")
        return redirect("products:home")



# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION  
    
def checkout(request):
    
    
        
    if request.method == 'POST' and 'btn_stripe' in request.POST :
    
        success_url =  request.build_absolute_uri(reverse("orders:success_payment"))
        cancel_url = request.build_absolute_uri(reverse("orders:cancel_payment"))
       
       
        # Stripe checkout session data
        session_data = {
        'mode': 'payment',
        'success_url': success_url,
        'cancel_url': cancel_url,
        'line_items': []
        }
        # add order items to the Stripe checkout session
        for item in Order.objects.all():
            session_data['line_items'].append({
            'price_data': {
                            'unit_amount': int(item.order.price * Decimal('100') ),
                            'currency': 'mad',
                            'product_data': {'name': item.order.title,},
                          },
            'quantity': item.quantity,
            })
            
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)
       
    order = Order.objects.all()
    total = sum(item.quantity*item.order.price for item in order) 
    compon_discount = request.session.get('compon_discount')
        
    if compon_discount :
    
        final_total = total - (compon_discount * initial_total / 100)
        return render(request,"orders/checkout.html", {'order':order,'total':final_total,'subtotal':total,'discount':compon_discount})
   
    
    
    return render(request,"orders/checkout.html",{'orders':order,'subtotal':total,'total':total})
    
    
    
 
    
def success_payment(request):
    for item in Order.objects.all():
           
            item.delete()
    return render(request, 'orders/success_payment.html')
        
        
        
def cancel_payment(request):
    order_id = request.session.get('order')
    order = Checkout.objects.get(id =order_id)
    order.delete()
    return render(request, 'orders/cancel_payment.html')
        