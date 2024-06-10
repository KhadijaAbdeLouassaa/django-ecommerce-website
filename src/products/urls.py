from django.contrib import admin
from django.urls import path
from . import views
from . import api 
# creat your urls 

app_name = 'products'

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('products/', views.products, name= 'products'),
    path('product_detail/<slug>/', views.product_detail, name= 'product_detail'),
    path('categories/<str:ctg_id>/', views.categories, name= 'categories'),
    path('search_product/', views.search_product, name= 'search_product'),
    
    path('favorite_products_page/',views.favorite_products_page, name = 'favorite_products_page'),
    path('add_to_favorites/<slug>/',views.add_to_favorites, name = 'add_to_favorites'),
    path('remove_from_favorites/<slug>/',views.remove_from_favorites, name = 'remove_from_favorites'),
    
    path('contact/', views.contact, name= 'contact'),
    
    path('product_list_api/', api.product_list_api, name= 'product_list_api'),
]