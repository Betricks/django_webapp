from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import PostsForm, CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import Posts, UserProfile, User
from django.contrib.auth.models import User
from .decorators import admin_only
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Q


# Create your views here.

@login_required(login_url='login')
def home(request, id):
    posts = Posts.objects.get(pk=id)
    liked = None
    user = request.user

    if posts.likes.filter(id=user.id).exists():
        liked = True

    if request.method == 'POST':
        if posts.likes.filter(id=user.id).exists():
            posts.likes.remove(user)
            like = False

        else:
            posts.likes.add(user)
            like = True
                

    mydata = Posts.objects.all()
    context = {
        'posts':mydata,
        'liked': liked,
    }
    return render(request, 'Blogs/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            user = form.save()
            group = Group.objects.get(name='User')
            user.groups.add(group)
            
            login(request, user)
            return redirect('home')
        else:
            print('invalid')
            form = CustomUserCreationForm()

            
    else:
        form = CustomUserCreationForm()

    return render(request, 'Blogs/signin.html', {'forms': form})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        password = request.POST.get('passwords')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            print('invalid cridentials ')
        
    return render(request, 'Blogs/login.html')



def logoutview(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createpost(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            Mypost = form.save(commit=False)
            Mypost.auther = request.user
            Mypost.save()
            return redirect('home')
        else:
            form = PostsForm()
    form = PostsForm()
            
    return render(request, 'Blogs/posts.html', {'form': form})

@login_required(login_url='login')
def update(request, id):
    post_update = Posts.objects.get(pk=id)    
    if request.method == "POST":
        form = PostsForm(request.POST, instance=post_update)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = PostsForm(instance=post_update)
    
    return render(request, 'Blogs/posts.html', {'form':form})       



@login_required(login_url='login')
def admin(request):
    return render(request, 'Blogs/admin.html') 

     
 
@login_required(login_url='login')       
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    
    return render(request, 'Blogs/password.html', context)



@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_pro = form.save(commit=False)
            user_pro.user_profile = request.user
            user_pro.save()
            return redirect('home')
            
    else:
        form = UserProfileForm()   
    return render(request, 'Blogs/profile.html', {'forms': form})


@login_required(login_url='login')
def updateProfile(request, id):
    profiel_update = UserProfile.objects.get(pk=id)   
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profiel_update)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = UserProfile(instance=profiel_update)

    context = {
        'forms': form
            }
    return render(request, 'Blogs/profile.html', context)       



def searching(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        if q is not ' ' or q is not None:
            multi_q = Posts.objects.filter(Q(BlogPost__icontains=q))
            if multi_q is None:
                return HttpResponce('does not exist ')
        else:
            return HttpResponce("does not exist ")
    context = {
        'datas': multi_q
    }

    return render(request, 'Blogs/search.html', context)
