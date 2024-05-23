from django.contrib import admin
from django.urls import path
from . import views
# creat your urls here

app_name = 'accounts'


urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.signin, name = 'login'),
    path('logout/',views.logouted, name = 'logout'),
    
    path('reset_password/',views.reset_password, name = 'reset_password'),
    path('password_reset_sent/',views.password_reset_sent, name = 'password_reset_sent'),
    path('password_reset_form/<token>/',views.password_reset_form, name = 'password_reset_form'),
    
    path('user_profile/',views.user_profile, name = 'user_profile'),
    
    
]