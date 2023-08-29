from django.contrib.auth.models import User
from django.db import models
from utils.generate_code import generate_code

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='accounts', blank=True, null=True)
    address = models.CharField(max_length=200)
    code = models.CharField(max_length=10,default=generate_code)
    # Add other fields you want in the user profile

    def __str__(self):
        return str(self.user)

