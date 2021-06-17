from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('product-details', ProductDetailsView.as_view(), name='product-details'),
    path('shop', ShopDetailsView.as_view(), name='shop'),
    path('signup',register, name = 'signup'),
    path('signin',signin, name = 'signin'),
    path('contact',contact, name = 'contact'),
    path('blog',BlogDetailsView.as_view(), name = 'blog'),
    path('blog-single',BlogSingleDetailsView.as_view(), name = 'blog-single'),
    path('shop', shop, name='shop'),
    path('checkout',checkout, name = 'checkout'),
    path('mycart', ViewCart.as_view(), name='mycart'),
    path('login', login, name='login'),
    path('404', error, name='404'),
    path('add-to-cart/<slug>', cart, name='add-to-cart'),
    path('delete-cart/<slug>', deletecart, name='delete-cart'),
    path('delete-single-cart/<slug>', delete_single_cart, name='delete-single-cart'),
    path('review',review, name='review'),
    path('checkout',CheckoutView.as_view(),name='checkout'),
]

