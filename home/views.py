from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic.base import View

from home.models import Category, Slider, Brand, Item, Contact, ContactInformation, Cart, Review, Blog, Post, Comment
from django.core.mail import EmailMultiAlternatives


class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['items'] = Item.objects.all()
        self.views['new_items'] = Item.objects.filter(label = 'new')
        self.views['hot_items'] = Item.objects.filter(label = 'hot')
        self.views['sale_items'] = Item.objects.filter(label = 'sale')

        return render(request,'index.html',self.views)

class ProductDetailsView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['items'] = Item.objects.all()
        self.views['productdetails_items'] = Item.objects.filter(label = 'productdetails')
        self.views['profile_items'] = Item.objects.filter(label='profile')
        self.views['tag_items'] = Item.objects.filter(label='tag')
        self.views['new_items'] = Item.objects.filter(label='new')

        return render(request,'product-details.html',self.views)



def review(request):
    view = {}
    if request.method == "POST":
        subject = request.POST['subject']
        comment = request.POST['comment']

        data = Review.objects.create(
            subject = subject,
            comment= comment
        )
        data.save()
        view['success'] = "The message is submitted."

    return render(request, 'review.html', view)

class ShopDetailsView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['hot_items'] = Item.objects.filter(label='hot')
        self.views['new_items'] = Item.objects.filter(label='new')
        self.views['sale_items'] = Item.objects.filter(label='sale')

        return render(request,'shop.html',self.views)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'The username is already used.')
                return redirect('home:signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already used.')
                return redirect('home:signup')
            else:
                data = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password
                )
                data.save()
                messages.error(request, 'You are signed up.')
                return redirect('home:signup')

        else:
            messages.error(request, 'Password does not match each other.')
            return redirect('home:signup')

    return render(request,'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Username and password do not match.')
            return redirect('home:signin')

    return render(request,'signin.html')

class BlogDetailsView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['new_blog'] = Blog.objects.filter(label='new')
        self.views['hot_blog'] = Blog.objects.filter(label='hot')
        self.views['sale_blog'] = Blog.objects.filter(label='sale')

        return render(request,'blog.html',self.views)

class BlogSingleDetailsView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['new_blog'] = Blog.objects.filter(label='new')
        self.views['posts'] = Post.objects.filter()
        self.views['comments'] = Comment.objects.filter()

        return render(request,'blog-single.html',self.views)


def shop(request):
    return render(request,'shop.html')

def checkout(request):
    return render(request,'checkout.html')

def login(request):
    return render(request,'login.html')

def error(request):
    return render(request,'404.html')

class ViewCart(BaseView):
    def get(self, request):
        self.views['carts'] = Cart.objects.filter(user = request.user.username)

        return render(request,'cart.html',self.views)

def cart(request,slug):
    if Cart.objects.filter(slug = slug, user = request.user.username).exists():
        quantity = Cart.objects.get(slug = slug, user = request.user.username).quantity
        quantity = quantity +1
        price = Item.objects.get(slug = slug).price
        discounted_price = Item.objects.get(slug = slug).discounted_price
        if discounted_price >0:
            total = discounted_price * quantity
        else:
            total = price * quantity
        Cart.objects.filter(slug=slug, user=request.user.username).update(quantity = quantity, total = total)

    else:
        price = Item.objects.get(slug = slug).price
        discounted_price = Item.objects.get(slug = slug).discounted_price
        if discounted_price >0:
            total = discounted_price
        else:
            total = price

        data = Cart.objects.create(
            user = request.user.username,
            slug = slug,
            item = Item.objects.filter(slug = slug)[0],
            total = total
        )
        data.save()

    return redirect('home:mycart')

def  deletecart(request,slug):
    if Cart.objects.filter(slug= slug, user = request.user.username).exists():
        Cart.objects.filter(slug=slug, user=request.user.username).delete()
        messages.success(request,'The item is deleted.')
    return redirect("home:mycart")

def delete_single_cart(request,slug):
    if Cart.objects.filter(slug = slug, user = request.user.username).exists():
        quantity = Cart.objects.get(slug = slug, user = request.user.username).quantity
        quantity = quantity -1
        price = Item.objects.get(slug=slug).price
        discounted_price = Item.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            total = discounted_price * quantity
        else:
            total = price * quantity

        Cart.objects.filter(slug=slug, user=request.user.username).update(quantity = quantity, total = total)

        return redirect("home:mycart")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        messages.success(request,"Message is submitted.")
        html_content = f"<p> The customer having name {name}, mail address {email} and subject {subject} has some message and the message is {message}."
        msg = EmailMultiAlternatives(subject, message, 'neelarai941@gmail.com', ['neelarai941@gmail.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    return render(request,'contact-us.html')


def contact(request):
    view = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        view['success'] = "The message is submited."

    view['info'] = ContactInformation.objects.all()

    return render(request,'contact-us.html',view)








