from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='accounts', blank=True, null=True)
    address = models.CharField(max_length=200)
    # Add other fields you want in the user profile

    def __str__(self):
        return str(self.user)

