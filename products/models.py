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
    
    
    

