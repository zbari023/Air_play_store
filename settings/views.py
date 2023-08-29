from django.shortcuts import render
from products.models import Products
# Create your views here.

def home(request):
    products = Products.objects.all()[:12] # just for limit products
    
    return render(request,'settings/home.html',{'products':products})

def about(request):
    pass