from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddArticleForm
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

def add_article(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            article_form = AddArticleForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
            if article_form.is_valid():
                article = article_form.save(commit=False)
                article.author = request.user  # Assign the current user as the author
                article.save()
                messages.success(request, "Article added successfully!")
                return redirect('home')
        else:
            article_form = AddArticleForm()  # Create an empty form for GET requests
        return render(request, 'add_article.html', {'form': article_form})
    else:
        messages.error(request, "You must be logged in to view that page.")
        return redirect('home')