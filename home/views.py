from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from home.models import Category, Slider, Brand, Item, Contact, ContactInformation


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

def blog(request):
    return render(request,'blog.html')

def blogsingle(request):
    return render(request,'blog-single.html')

def shop(request):
    return render(request,'shop.html')

def product_details(request):
    return render(request,'product-details.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')

def login(request):
    return render(request,'login.html')

def error(request):
    return render(request,'404.html')








