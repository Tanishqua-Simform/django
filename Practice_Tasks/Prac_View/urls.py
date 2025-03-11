from django.urls import path
from .views import hello_name, greeting, WelcomeTemplateView, StudentDetailView, redirect_greeting, RequestMethodsView, json_response, ProductDetailView, dashboard, CustomLogicView

urlpatterns = [
    path('hello/<str:name>', hello_name, name='hello_name'),
    path('greeting', greeting, name='greeting'),
    path('welcome', WelcomeTemplateView.as_view(), name='WelcomeTemplateView'),
    path('detail/<pk>', StudentDetailView.as_view(), name='StudentDetailView'),
    path('redirect', redirect_greeting, name='redirect_greeting'),
    path('method', RequestMethodsView.as_view(), name='RequestMethodsView'),
    path('json', json_response, name='json_response'),
    path('product/<pk>', ProductDetailView.as_view(), name='ProductDetailView'),
    path('dashboard', dashboard, name='dashboard'),
    path('<int:id>', CustomLogicView.as_view(), name='CustomLogicView'),
]
