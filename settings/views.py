from django.shortcuts import render
from products.models import Products
# Create your views here.

def home(request):
    products = Products.objects.all()[:12] # just for limit products
    
    return render(request,'settings/home.html',{'products':products})

def about(request):
    return render(request,'settings/about.html',{})

def why(request):
    return render(request,'settings/why.html',{})

def testimonial(request):
    return render(request,'settings/testimonial.html',{})

def profiluser(request):
    return render(request,'settings/profil_user.html',{})