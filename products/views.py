from django.shortcuts import render
from .models import Products , Customer
from django.views import generic

# Create your views here.


class ProductList(generic.ListView):
    model = Products