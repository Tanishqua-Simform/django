from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, View
from .models import Student, Product

# Create your views here.
def hello_name(request, name):
    html = f"<h1>Hello, {name}!</h1>"
    return HttpResponse(html)

def greeting(request):
    context = { 'greeting': 'Good Morning' }
    return render(request, 'Prac_View/greeting.html', context)

class WelcomeTemplateView(TemplateView):
    template_name = "Prac_View/welcome.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["user"] = "John"
        return context
    
class StudentDetailView(DetailView):
    model = Student
    template_name = "Prac_View/student_detail.html"

def redirect_greeting(request):
    return redirect(reverse("greeting"))

@method_decorator(csrf_exempt, name='dispatch')
class RequestMethodsView(View):
    def get(self, request):
        return HttpResponse('This is a GET Request')
    
    def post(self, request):
        return HttpResponse('This is a POST Request')
    
def json_response(request):
    data = {'status': 'success', 'message': 'Data received'}
    return JsonResponse(data)

class ProductDetailView(DetailView):
    model = Product
    template_name = "Prac_View/product_detail.html"

    def get_object(self, queryset = None):
        try:
            return super().get_object(queryset)
        except Product.DoesNotExist:
            raise Http404("Product Not Found")

@login_required
def dashboard(request):
    return HttpResponse("This is your dashboard!")

class CustomLogicView(View):
    def get(self, request, id):
        html = "Even ID" if id % 2 == 0 else "Odd ID"
        return HttpResponse(html)

