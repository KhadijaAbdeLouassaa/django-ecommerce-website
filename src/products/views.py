from django.shortcuts import render,redirect,reverse
from .models import Product,ProductReview,Categories
from accounts.models import UserProfile
from blog.models import Blog
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils import timezone
# Create your views here.


def home(request):
    product = Product.objects.all()
    latest_products = Product.objects.filter(added_at__month=(datetime.now().month)-1 )
    blog = Blog.objects.all()
    for post in blog :
        post.comment_count = post.comment_set.count()
    context = {'product':product,
                'latest_products':latest_products,
                'blog':blog,
               
                }
    return render(request, "products/home.html",context)
    
    
def search_product(request):
    if 'q' in request.GET:
        search = Product.objects.filter(title__icontains= request.GET['q'])
        paginator = Paginator(search,6)
        page_num = request.GET.get('page')
        searched = paginator.get_page(page_num)
        return render(request,"products/search_product.html",{'searched':searched,'search':search})
    else:
        search = Product.objects.all()
        paginator = Paginator(search,6)
        page_num = request.GET.get('page')
        searched = paginator.get_page(page_num)
        return render(request,"products/search_product.html",{'searched':searched,'search':search})

 
def products(request):
    items = Product.objects.all()
    paginator = Paginator(items,6)
    page_num = request.GET.get('page')
    product = paginator.get_page(page_num)
    latest_products = Product.objects.filter(added_at__month=(datetime.now().month) )
    for item in items :
        if item.discount > 0 :
            item.discount_percent = 100 * (item.price-item.discount )//item.price
            
   
    
    return render(request,"products/products.html",{'product':product,'items':items,'latest_products':latest_products})
    
    
def product_detail(request,slug):
    product = Product.objects.get(slug = slug)
    related_pro = Product.objects.filter(category = product.category)
    reviews = ProductReview.objects.filter(product=product)
        
    return render(request,"products/product_detail.html",{'product':product,'related_pro':related_pro,'reviews':reviews})
   
   
def add_reviews(request, slug):
    product = Product.objects.get(slug = slug)
    if request.user.is_authenticated :
        if request.method == 'POST' and 'user_review' in request.POST : 
            user_review = request.POST['user_review']
            if user_review :
                ProductReview.objects.create(user=request.user,product=product,reviews=user_review)
    else : messages.add_message(request,messages.ERROR, "Please login ")
    
    return redirect('products:product_detail',slug=slug)  
   
   
def categories(request, ctg_id):
    category = Categories.objects.get(name = ctg_id )
    product = Product.objects.filter(category=category)
    
    paginator = Paginator(product,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products/categories.html",{'product':page_obj,'category_name':product})
    
    
def favorite_products_page(request):  
    if request.user.is_authenticated :
        user = UserProfile.objects.get(user= request.user)
        items = user.favorite_products.all()
        paginator = Paginator(items,6)
        page_number = request.GET.get('page')
        favorite_product = paginator.get_page(page_number)
        
        return render(request,"products/favorite_products.html", {'favorite_product':favorite_product,'items':items})
    else :
        messages.add_message(request,messages.ERROR, "Please login ")
        return redirect("products:home")
    
    
def add_to_favorites(request, slug):
    if request.user.is_authenticated :
        favorite_product = Product.objects.get(slug=slug)
        if UserProfile.objects.filter(user=request.user,favorite_products=favorite_product).exists() :            
            pass
        else :
            user = UserProfile.objects.get(user = request.user)
            user.favorite_products.add(favorite_product)
            now = timezone.now()
       
    else :
        messages.add_message(request,messages.ERROR, "Please login ")
      
    return redirect('products:product_detail',slug=slug) 

    
def remove_from_favorites(request, slug):
    product = Product.objects.get(slug=slug)
    user = UserProfile.objects.get(user = request.user)
    user.favorite_products.remove(product)
            
    return redirect("products:favorite_products_page")
    
     
def contact(request):
    if request.method == 'POST' and 'btn_send_msg' in request.POST :
        username = None
        user_email = None
        user_message = None
        if 'username' in request.POST : username= request.POST['username']
        if 'user_email' in request.POST : user_email= request.POST['user_email']
        if 'user_message' in request.POST : user_message= request.POST['user_message']        
        print(user_email)
        if username and user_email and user_message :
            EmailMessage("oganiwebsite message",
                         f"from {username}\n {user_email}\n message:\n{user_message}",
                         user_email,
                         ['to_addrss@gmail.com'],
                         ).send()
        else :
            messages.add_message(request,messages.ERROR, "please full all ")
 
    return render(request,"contact\contact.html")