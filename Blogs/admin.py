from django.contrib import admin
from .models import UserProfile, User, Posts
# Register your models here.

admin.site.register(User)
admin.site.register(Posts)