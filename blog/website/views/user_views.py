from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from ..forms import SignUpForm
from ..models import Article
from django.contrib.auth.models import User
from django.db.models import Q

def home(request):
    search_query = request.GET.get('search_query')
    articles = Article.objects.all()

    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query)
        )

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
        return render(request, 'user/home.html', {'articles':articles, 'search_query': search_query})



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
    
    return render(request, 'user/register.html', {'form': form})


def user_detail(request, pk):
    if request.user.is_authenticated:
        user_detail = get_object_or_404(User, id=pk)
        articles = Article.objects.filter(author=user_detail)

        context = {
            'user_detail': user_detail,
            'articles': articles,
        }

        return render(request, 'user/user_detail.html', context)
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')

def delete_user(request, pk):
    if request.user.is_authenticated:
        delete_account = get_object_or_404(User, id=pk)
        if delete_account == request.user:
            # Log out the user before deleting the account
            logout(request)
            delete_account.delete()
            messages.success(request, "Account deleted successfully!")
            return redirect('home')
        else:
            messages.error(request, "You do not have permission to delete this account.")
    else:
        messages.error(request, "You must be logged in to delete an account.")
    return redirect('home')


def update_user(request, pk):
    if request.user.is_authenticated:
        current_account = get_object_or_404(User, id=pk)
        if current_account == request.user:
            user_form = SignUpForm(request.POST or None, instance=current_account)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Account has been successfully updated !")
                return redirect('user_detail', pk=current_account.pk) 
            
            return render(request, 'user/update_user.html', {'form':user_form, 'current_account': current_account})
        else:
            messages.error(request, "Something went wrong, try again later.")
            return redirect('home')

