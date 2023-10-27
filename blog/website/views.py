from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.models import User



def home(request):
    articles = Article.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Login Successful. Welcome back {username} !")
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



def delete_article(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, id=pk)
        if article.author == request.user:
            article.delete()
            messages.success(request, "Article deleted successfully!")
            return redirect('home')
        else:
            messages.error(request, "You are not authorized to delete this article.")
            return redirect('home')



def article_detail(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, id=pk)
        comments = Comment.objects.filter(article=article)
        comment_form = CommentForm()

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.article = article
                new_comment.author = request.user
                new_comment.save()
                comment_form = CommentForm()  # Clear the form

        return render(request, 'article.html', {'article': article, 'comments': comments, 'comment_form': comment_form})
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')



def user_detail(request, pk):
    if request.user.is_authenticated:
        user_detail = get_object_or_404(User, id=pk)
        articles = Article.objects.filter(author=user_detail)

        context = {
            'user_detail': user_detail,
            'articles': articles,
        }

        return render(request, 'user_detail.html', context)
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')