from django.contrib import admin
from .models import Order,Checkout
# Register your models here.


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user','order', 'quantity', 'added_at']
    
    
    
@admin.register(Checkout)
class CheckoutModelAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number', 'city', 'paid']
    