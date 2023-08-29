from django.contrib import admin
from .models import UserProfile
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']
    search_fields = ['user']
admin.site.register(UserProfile, ProductAdmin)
