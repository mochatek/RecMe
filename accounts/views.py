from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def req_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user = user)
            return redirect('movies:index')
        else:
            messages.error(request,'Username-Password Mismatch.')
            return redirect('accounts:login')


def req_signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = User.objects.create_user(username = username, password = password)
            return redirect('accounts:login')


@login_required(login_url = 'accounts:login')
def req_logout(request):
    logout(request)
    return redirect('accounts:login')
