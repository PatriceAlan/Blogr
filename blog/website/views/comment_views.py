from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..forms import CommentForm
from ..models import Comment

def delete_comment(request, pk):
    if request.user.is_authenticated:
        comment_delete = get_object_or_404(Comment, id=pk)
        if comment_delete.author == request.user:
            comment_delete.delete()
            messages.success(request, "Comment deleted successfully!")

            article = comment_delete.article
            return redirect('article_detail', pk=article.pk) 
        else:
            messages.error(request, "Something went wrong, try again later.")
            return redirect('home')

def update_comment(request, pk):
    if request.user.is_authenticated:
        current_comment = get_object_or_404(Comment, id=pk)
        current_article = current_comment.article
        if current_comment.author == request.user:
            comment_form = CommentForm(request.POST or None, instance=current_comment)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request, "Comment has been successfully updated!")
                return redirect('article_detail', pk=current_article.pk)
            return render(request, 'comment/update_comment.html', {'form': comment_form, 'current_article': current_article})
        else:
            messages.error(request, "Something went wrong, try again later.")
            return redirect('home')
