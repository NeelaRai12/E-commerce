from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.urls import reverse

STATUS = (('In', 'In Stock'), ('Out', 'Out of Stock'))
LABEL = (('new', 'New Product'), ('hot', 'Hot Product'), ('sale', 'Sale Product'))


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to= 'media')

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to= 'media')
    description = models.TextField()
    url = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to= 'media')

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.CharField(max_length=300, unique=True)
    discounted_price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS)
    label = models.CharField(max_length=60, choices=LABEL, default='new')
    image = models.ImageField(upload_to= 'media')

    def __str__(self):
        return self.title

    def get_cart_url(self):
        return reverse("home:add-to-cart", kwargs={'slug':self.slug})



class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length= 200)
    subject = models.CharField(max_length= 500)
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactInformation(models.Model):
    name = models.CharField(max_length= 300, blank= True)
    address = models.CharField(max_length= 300)
    tole = models.CharField(max_length= 300)
    contact_no = models.CharField(max_length= 300)
    fax_no = models.CharField(max_length= 300)
    email = models.CharField(max_length= 300)

    def __str__(self):
        return self.name

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    slug = models.CharField(max_length= 200)
    quantity = models.IntegerField(default= 1)
    user = models.CharField(max_length= 200)
    date = models.DateTimeField(auto_now= True)
    total = models.IntegerField(null= True)

    def __str__(self):
        return self.user

    def delete_get_cart_url(self):
        return reverse("home:delete-cart", kwargs={'slug':self.slug})

    def delete_single_cart_url(self):
        return reverse("home:delete-single-cart", kwargs = {'slug':self.slug})


#
# class Comment(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     item = models.ForeignKey(Item,on_delete=models.CASCADE)
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     subject = models.CharField(max_length= 50, blank= True)
#     comment = models.CharField(max_length= 250, blank= True)
#     rate = models.IntegerField(default=1)
#     ip = models.TextField(max_length= 20,blank= True)
#     status = models.CharField(max_length= 10,choices=STATUS,default='New')
#     create_at = models.DateTimeField(auto_now=True)
#     update_at = models.DateTimeField(auto_now= True)
#
#     def __str__(self):
#         self.subject
#
#
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['subject', 'comment', 'rate']

class Review(models.Model):
    subject = models.CharField(max_length= 50, blank= True)
    comment = models.CharField(max_length= 250, blank= True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.subject


class Blog(models.Model):
    title = models.CharField(max_length= 50)
    date = models.DateTimeField(auto_now= True)
    time = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=50, choices=STATUS, null=True)
    label = models.CharField(max_length=60, choices=LABEL, default='new')
    image = models.ImageField(upload_to='media')
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

