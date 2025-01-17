from django.shortcuts import render,redirect
from .models import Coupon
from django.utils import timezone
from django.contrib import messages
# Create your views here.



def coupon(request):
    now = timezone.now()
    if request.method == 'POST' and 'coupon' in request.POST:
        code = request.POST['coupon']
        if code:            
            try :
                the_coupon = Coupon.objects.get(code__iexact = code,
                                                valid_from__lte = now,
                                                valid_to__gte = now,
                                                active = True)
                request.session['coupon_discount'] = the_coupon.discount
                # final_total = shoping_cart(request)
                return redirect("orders:shoping_cart")
             
            except Coupon.DoesNotExist :
                messages.add_message(request,messages.ERROR,"This coupon dosen't exist ")
                          
        else :
            messages.add_message(request,messages.ERROR,"please, enter a coupon ")
     
        
    return redirect("orders:shoping_cart")

