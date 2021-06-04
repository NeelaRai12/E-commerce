from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('signup',register, name = 'signup'),
    path('signin',signin, name = 'signin'),
    path('contact',contact, name = 'contact'),
    path('blog',blog, name = 'blog'),
    path('blog-single',blogsingle, name = 'blog-single'),
    path('shop', shop, name='shop'),
    path('product-details',product_details, name = 'product-details'),
    path('checkout',checkout, name = 'checkout'),
    path('cart', cart, name='cart'),
    path('login', login, name='login'),
    path('404', error, name='404'),
]
