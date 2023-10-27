from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..forms import AddArticleForm, CommentForm
from ..models import Article, Comment

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
        article_delete = get_object_or_404(Article, id=pk)
        if article_delete.author == request.user:
            article_delete.delete()
            messages.success(request, "Article deleted successfully!")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong, try again later.")
            return redirect('home')

def update_article(request, pk):
    if request.user.is_authenticated:
        current_article = get_object_or_404(Article, id=pk)
        if current_article.author == request.user:
            article_form = AddArticleForm(request.POST or None, instance=current_article)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, "Article has been successfully updated !")
                return redirect('home')
            return render(request, 'update_article.html', {'form':article_form})
        else:
            messages.error(request, "Something went wrong, try again later.")
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