from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Products
from accounts.models import UserProfile
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


@login_required
def profiluser(request):
    user_profile = request.user.user_profile

    # Retrieve the profile fields
    bio = user_profile.bio
    profile_picture = user_profile.profile_picture
    address = user_profile.address
    code = user_profile.code

    # Add other fields you want to retrieve

    return render(request, 'settings/profil_user.html', {
        'user_profile' : user_profile ,
        'bio': bio,
        'profile_picture': profile_picture,
        'address': address,
        'code': code,
        # Add other fields you want to pass to the template
    })