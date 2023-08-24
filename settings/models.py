from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=40)
    email_us = models.CharField(max_length=25, null=True , blank=True)
    subtitle = models.TextField(max_length=200, null=True , blank=True)
    phones = models.TextField(max_length=200, null=True , blank=True)
    address = models.TextField(max_length=200, null=True , blank=True)
    fb_link = models.URLField(null=True , blank=True)
    insta_link = models.URLField(null=True , blank=True)
    x_link = models.URLField(null=True , blank=True)
    youtube_link = models.URLField(null=True , blank=True)

    
    def __str__(self):
        return self.name
    