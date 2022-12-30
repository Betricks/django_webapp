from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.home, name='postView'),
    path('sign-in/', views.signup, name='sign_up'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('create-post/', views.createpost, name='createpost'),
    path('update-post/<int:id>/', views.update, name='update'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/<int:id>/', views.updateProfile, name='updateProfile'),
    path('add/', views.admin, name='add'),
    path('change-password/', views.change_password, name='changepassword'),
    path('search/', views.searching, name='search')
    
    
]


