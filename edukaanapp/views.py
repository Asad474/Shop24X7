from django.shortcuts import render, redirect
from .decorators import unauthenticated_user
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from edukaanproject import settings

# Create your views here.
def home(request):
    return render(request, 'edukaanapp/home.html')


@unauthenticated_user
def sigin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        valuenext= request.GET.get('next')
        print(valuenext)

        try:
            user = authenticate(request, email = email, password = password)
            login(request, user)
            if valuenext == '' or valuenext == None:
                return redirect('home')
            return redirect(valuenext)

        except:
            messages.error(request, 'Email or Password is invalid!!!')

    return render(request,'edukaanapp/signin.html')


def signout(request):
    logout(request)
    return render(request, 'edukaanapp/home.html')


@unauthenticated_user
def signup(request):
    form = SignUpForm()

    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid:                
                user = form.save(commit = False)
                form.save()
                messages.success(request, f'Hi {user.username}, thank you for registering!!!')
                return redirect('signin')

    except:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        all_users_email = MyUser.objects.all().values('email')
        all_users_username = MyUser.objects.all().values('username')

        if {'usernaem' : username} in all_users_username:
            messages.error(request, 'User with this username already exists!!!')     

        elif {'email' : email} in all_users_email:
            messages.error(request, 'User with this email id already exists!!!')    

        elif password1 != password2:
            messages.error(request, 'Password and Confirm Password are not matching with each other!!!')

        else:
            messages.error(request ,'Something went wrong,try again!!!')    

        return redirect('signup')

    context={'form' : form}
    return render(request, 'edukaanapp/signup.html', context)


@login_required(login_url = 'signin')
def registerShop(request):
    form = RegisterShop()

    if request.method == 'POST':
        form = RegisterShop(request.POST)
        if form.is_valid:
            f = form.save(commit = False)
            Shop.objects.create(
                user = request.user,
                name = f.name,
                category = f.category,
                opening_time = f.opening_time,
                closing_time = f.closing_time,
                address = f.address,
                state = f.state,
                city = f.city,
                pincode = f.pincode
            )

            return redirect('home')
        
    context = {'form' : form}
    return render(request, 'edukaanapp/registerShop.html', context)


@login_required(login_url = 'signin')
def addItem(request, pk):
    form = AddItemForm()

    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        shop = Shop.objects.get(id = pk)

        if form.is_valid:
            f = form.save(commit = False)
            Product.objects.create( 
                shop = shop,
                category = shop.category,
                image = f.image,
                name = f.name,
                price = f.price,
                description = f.description
            )

            return redirect('home')

    context = {'form' : form}
    return render(request, 'edukaanapp/additem.html', context)


@login_required(login_url = 'signin')
def shopdetails(request, pk):
    shop = Shop.objects.get(id = pk)
    products = shop.product_set.all()
    context = {'shop' : shop, 'products' : products}
    return render(request, 'edukaanapp/sellerItems.html', context)