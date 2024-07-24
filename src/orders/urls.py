from django.contrib import admin
from django.urls import path
from . import views


app_name = 'orders'


urlpatterns = [
    path('shoping_cart/',views.shoping_cart, name= 'shoping_cart'),
    path('add_to_cart/<slug>/',views.add_to_cart, name= 'add_to_cart'),
    path('remove_from_cart/<int:id>/',views.remove_from_cart, name= 'remove_from_cart'),
    path('checkout/',views.checkout, name= 'checkout'),
    path('success_payment/',views.success_payment, name= 'success_payment'),
    path('cancel_payment/',views.cancel_payment, name= 'cancel_payment'),
]
