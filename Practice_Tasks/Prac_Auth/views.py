from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def dashboard(request):
    return HttpResponse("<h1>Welcome to Dashboard!</h1>")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    else:
        form = RegisterForm()
    return render(request, 'Prac_Auth/register.html', {'form': form})

def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('auth_dashboard')
    form = LoginForm()
    return render(request, 'Prac_Auth/login.html', {'form': form})

def logout_form(request):
    logout(request)
    return redirect('home')

@login_required(login_url="auth_login")
def profile(request):
    user = User.objects.get(username=request.user)
    html = f'<h1>Profile:</h1><h3>{user.username} ({user.email})</h3>'
    return HttpResponse(html)