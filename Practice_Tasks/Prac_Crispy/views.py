from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm, ContactForm, LoginForm, ProfileForm, RegistrationForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Form submitted successfully</h1>")
    else:
        form = FeedbackForm()
    return render(request, "Prac_Crispy/feedback.html", {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Form submitted successfully</h1>")
    else:
        form = ContactForm()
    return render(request, "Prac_Crispy/contact.html", {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Form submitted successfully</h1>")
    else:
        form = LoginForm()
    return render(request, "Prac_Crispy/login.html", {'form': form})

def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Form submitted successfully</h1>")
    else:
        form = ProfileForm()
    return render(request, "Prac_Crispy/profile.html", {'form': form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Form submitted successfully</h1>")
    else:
        form = RegistrationForm()
    return render(request, "Prac_Crispy/register.html", {'form': form})

