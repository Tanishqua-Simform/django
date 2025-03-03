from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello World from Django!')

def tani(request):
    return HttpResponse('Hello Tanishqua!')

def soham(request):
    return HttpResponse('Hello Soham!')

def lamha(request):
    return HttpResponse('Hello Lamha!')