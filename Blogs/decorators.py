from django.contrib.auth.models import Group
from django.shortcuts import redirect, render


def admin_only(view_func):
    def wrapper(*args, **kwargs):
        group = None
        if request.user.groups.exit():
            group = request.user.groups.all().name

        if group == "User":
            return redirect('home')

        if group == "admin":
            return redirect(request, *args, **kwargs)

        else:
            return redirect('home')
