from django.urls import path
from . import views
# start here

app_name = 'blog'


urlpatterns=[
    path('blog/',views.blog, name='blog'),
    path('blog_details/<slug>/',views.blog_details, name='blog_details'),
    path('categories/<str:ctgy_id>/',views.categories, name='categories'),
    path('search_blog/',views.search_blog, name='search_blog'),
    
    path('post_comment/<slug>/',views.post_comment, name='post_comment'),
]