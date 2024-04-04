from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'authentication/home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        my_user = User.objects.create_user(username, '', password)
        my_user.save()

        messages.success(request, 'Your account has been created')
        return redirect('login')

    return render(request, 'authentication/signup.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'authentication/login.html')


@login_required
def user_home(request):
    username = request.user.username
    return render(request, 'authentication/user_home.html', {'username': username})


def sign_out(request):
    logout(request)
    return redirect('home')
