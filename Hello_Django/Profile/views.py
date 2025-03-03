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