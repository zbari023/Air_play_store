from django.db import models
from django.utils import timezone
from accounts.models import UserProfile

# Create your models here.







class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
    
    

class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)  
    email = models.EmailField()
    total_price = models.FloatField(default=0)
    def __str__(self):
        return f"Order-{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"