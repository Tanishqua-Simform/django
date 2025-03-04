from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Profile Page</h1>')

def tani(request):
    return HttpResponse('This is <h1>Tanishqua`s</h1> Profile!')

def soham(request):
    return HttpResponse('This is <h1>Soham`s</h1> Profile!')

def lamha(request):
    return HttpResponse('This is <h1>Lamha`s</h1> Profile!')

# Creating templates to separate business logic(view) from static files(html, css)
def show_posts(request):
    return render(request, 'Profile/posts.html')

# Dynamic rendering of template
def show_likes(request):
    liked_by = {
        'p1': ['Lamha', 'Tanishqua', 'Yatri'],
        'p2': ['Soham', 'Rajesh', 'Meetu'],
        'p3': ['Meetu', 'Soham', 'Lamha'],
        'p4': ['Soham', 'Tanishqua'],
        'p5': [],       
        }
    return render(request, 'Profile/likes.html', context=liked_by)

# Link static files to template
def show_details(request):
    return render(request, 'Profile/details.html') 