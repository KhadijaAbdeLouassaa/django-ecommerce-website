from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import UserProfile
from django.contrib import messages
from .email_fct import send_email_fct
import uuid
from products.models import Product
# Create your views here.

def signup(request):
    if request.method == 'POST' and 'btn_signup' in request.POST :
        fullname = None
        phone_num = None
        email = None
        password1 = None
        password2 = None
        
        if "fullname" in request.POST : fullname = request.POST['fullname']
        if "phone_num" in request.POST : phone_num = request.POST['phone_num']
        if "email" in request.POST : email = request.POST['email']
        if "password1" in request.POST : password1 = request.POST['password1']
        if "password2" in request.POST : password2 = request.POST['password2']
        if fullname and phone_num and email and password1 and password2 :
            if User.objects.filter(username=fullname).exists():
                messages.add_message(request,messages.ERROR,"username alredy exist")
               
            elif User.objects.filter(email=email).exists():
                messages.add_message(request,messages.ERROR,"email alredy exist")
               
            else :
                if password1 == password2 :
                    user = User.objects.create_user(username=fullname,email=email,password=password2)
                    user.save
                    
                    userprofile = UserProfile(user=user, phone_number=phone_num)
                    userprofile.save()
                 
                    return redirect("accounts:login")
                else :
                    messages.add_message(request,messages.ERROR,"password must be same ")
                  
        else :
            messages.add_message(request,messages.ERROR, "please full all ")

    return render(request,"accounts/registration/signup.html")
    
def signin(request):

    if request.method == 'POST' and 'btn_login' in request.POST :
        
        fullname = request.POST['fullname']
        password = request.POST['password']
        
        if  fullname and  password :
            user = authenticate(username=fullname, password=password)
            if user is not None :
                login(request,user)
                return redirect("products:home")
                
            else :
                messages.add_message(request,messages.ERROR, " fullname or password doesn't correct")
        else :
            messages.add_message(request,messages.ERROR, "please full all ")
 
    return render(request,"accounts/registration/login.html")
    
    
def logouted(request): 
    
    logout(request)

    return redirect("products:home")


def reset_password(request): 
    if request.method == "POST" :
        email = request.POST['email']
        if email :
            if User.objects.filter(email=email).exists():
                token = str(uuid.uuid4())
                send_email_fct(email,token)
                return redirect("accounts:password_reset_sent")
                
            else :
                messages.add_message(request,messages.ERROR," no user has this email")
        else :
            messages.add_message(request,messages.ERROR, "please enter your email")
            
    return render(request,"accounts/registration/reset_password.html")
 
 
def password_reset_sent(request): 
    return render(request,"accounts/registration/password_reset_sent.html")
 
 
def password_reset_form(request,token): 
    if request.method == "POST" and "btn_done" :
        email = request.POST['email']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']
        if email and new_password and confirm_new_password :
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                return redirect("accounts:login")
                
            else :
                messages.add_message(request,messages.ERROR," no user has this email")
                
        else :
            messages.add_message(request,messages.ERROR, "please full all ")
            
    return render(request,"accounts/registration/password_reset_form.html")
 
 
def user_profile(request):
    if request.user.is_authenticated :
        user = UserProfile.objects.get(user= request.user)
        return render(request,"accounts/profile/user_profile.html",{'user':user})
        
    else :
        return redirect("products:home")
        





    
