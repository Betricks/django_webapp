from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth import validators

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=300, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True, default='defuilt/avatar.jpg')


    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.username + '\n' + self.email

class UserProfile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    Bio = models.CharField(max_length=9999)

    def __str__(self):
        return self.user_profile + '\n' + self.Bio




class Posts(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    BlogPost = models.TextField()
    VedioPost = models.FileField(upload_to="vedios/", null=True, blank=True)
    PhotePost = models.ImageField(upload_to='images/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='Blog_Post')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def total_likes(self):
        return self.BlogsPost + ' ' + self.likes.count()


    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.BlogPost