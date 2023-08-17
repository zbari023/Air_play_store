from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name





class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name