# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rentals.models import Property ,UserProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse ,HttpResponse


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        user_type= request.POST.get('user_type')
        # if user_type=="buyer":
        #     is_buyer=True
        # else:
        #     is_buyer=False
        # print(is_buyer,"IS BUyer")
        print(request.POST)
        
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()
        user_profile = UserProfile(user=user, phone_number=phone_number, user_type=user_type)
        user_profile.save()
        login(request, user)
        return redirect('index')
    return render(request, 'register/register.html')

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        user_type = request.POST['user_type']

        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            user = User.objects.filter(username=username_or_email).first()

        if user is not None and user.check_password(password):
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.user_type == user_type:
                login(request, user)
                if user_type == "buyer":
                    return redirect('buyer_dashboard')  # Replace with the actual URL name for buyer dashboard
                elif user_type == "seller":
                    return redirect('seller_dashboard')  # Replace with the actual URL name for seller dashboard
            else:
                return HttpResponse("Invalid user type")
        else:
            return HttpResponse("Invalid login details")
    return render(request, 'login/login.html')


def seller_dashboard(request):
    return render(request,'seller/seller_dashboard.html')

def buyer_dashboard(request):
    return render(request,'buyer/buyer_dashboard.html')



# def home(request):
#     properties = Property.objects.all()
#     return render(request, 'home.html', {'properties': properties})

# @login_required
# def post_property(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         location = request.POST['location']
#         area = request.POST['area']
#         bedrooms = request.POST['bedrooms']
#         bathrooms = request.POST['bathrooms']
#         nearby_hospitals = request.POST['nearby_hospitals']
#         nearby_colleges = request.POST['nearby_colleges']
#         property = Property(owner=request.user, title=title, description=description, location=location, area=area, bedrooms=bedrooms, bathrooms=bathrooms, nearby_hospitals=nearby_hospitals, nearby_colleges=nearby_colleges)
#         property.save()
#         return redirect('home')
#     return render(request, 'post_property.html')

# @login_required
# def my_properties(request):
#     properties = Property.objects.filter(owner=request.user)
#     return render(request, 'my_properties.html', {'properties': properties})

# @login_required
# def update_property(request, property_id):
#     property = Property.objects.get(id=property_id, owner=request.user)
#     if request.method == 'POST':
#         property.title = request.POST['title']
#         property.description = request.POST['description']
#         property.location = request.POST['location']
#         property.area = request.POST['area']
#         property.bedrooms = request.POST['bedrooms']
#         property.bathrooms = request.POST['bathrooms']
#         property.nearby_hospitals = request.POST['nearby_hospitals']
#         property.nearby_colleges = request.POST['nearby_colleges']
#         property.save()
#         return redirect('my_properties')
#     return render(request, 'update_property.html', {'property': property})

# @login_required
# def delete_property(request, property_id):
#     property = Property.objects.get(id=property_id, owner=request.user)
#     property.delete()
#     return redirect('my_properties')

# @login_required
# def like_property(request, property_id):
#     property = Property.objects.get(id=property_id)
#     property.likes += 1
#     property.save()
#     return JsonResponse({'likes': property.likes})
