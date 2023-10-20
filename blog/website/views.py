from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Article

# Create your views here.

def home(request):
    articles = Article.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful. Welcome back !")
            return redirect('home')
        else:
            messages.error(request, "Login Failed. Please check your credentials and try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'articles':articles})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful. Don't hesitate to come again!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful ! You can now log in using your credentials.")
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})
