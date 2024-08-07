from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Comment
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.



def blog(request): 
    paginator = Paginator(Blog.objects.all(),4)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    for post in posts :
        post.comment_count = post.comment_set.count()
    
    return render(request,"blog/blog.html",{'posts':posts})
    
    
    
def blog_details(request,slug):
    post_details = get_object_or_404(Blog,slug=slug)
    post = Blog.objects.all()        
    post_comments = Comment.objects.filter(post=post_details)# to get only that post comments
    
    return render(request,"blog/blog_detail.html",{'post_details':post_details,'post':post, 'post_comments':post_comments})
        
    
    
def categories(request, ctgy_id):
    category = Blog.objects.filter(category=ctgy_id)
    paginator = Paginator(category,4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request,"blog/categories.html",{'category':page_obj})
    
    
    
def search_blog(request):
    if 'q' in request.GET :
        search = Blog.objects.filter(title__icontains=request.GET['q'])
        paginator = Paginator(search,4)
        page_num = request.GET.get('page')
        searched = paginator.get_page(page_num)
        return render(request,"blog/search_blog.html",{'searched':searched})
        
    else :
        search = Blog.objects.all()
        paginator = Paginator(search,4)
        page_num = request.GET.get('page')
        searched = paginator.get_page(page_num)
        return render(request,"blog/search_blog.html",{'searched':searched})
        
        
        
        
def post_comment(request,slug):
    post =Blog.objects.get(slug=slug)
    if request.user.is_authenticated :
        if request.method == 'POST' and 'user_comment' in request.POST :
            if 'user_comment' in request.POST != '':
                comment = request.POST['user_comment']
                comment_add,created = Comment.objects.get_or_create(commenter= request.user, comment = comment ,post=post)
            else :
                messages.add_message(request,messages.ERROR, "Please write something")
                
            return redirect("blog:blog_details", slug=slug)        
              
    else :
       messages.add_message(request,messages.ERROR, "Please login ")
       return redirect("blog:blog_details", slug=slug)        
        
    
    
    
