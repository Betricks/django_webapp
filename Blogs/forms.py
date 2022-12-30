from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db.models import fields
from .models import Posts, UserProfile, User
from .validate import username_validate

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, validators=[username_validate])
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'mobile', 'age']



class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['BlogPost', 'VedioPost', 'PhotePost', 'likes']
