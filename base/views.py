from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user_login')
def index(request):
    return render(request, 'base/index.html')

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(username =un, password = pw)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'base/login.html')


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required(login_url='user_login')
def category(request):
    return render(request, 'base/category.html')


@login_required(login_url='user_login')
def product(request):
    return render(request, 'base/product.html')

@login_required(login_url='user_login')
def manage_category(request):
    return render(request, 'base/manage_category.html')

@login_required(login_url='user_login')
def manage_product(request):
    return render(request, 'base/manage_product.html')