from django.urls import path
from .views import feedback, contact, login, profile, register

urlpatterns = [
    path('feedback', feedback, name="feedback"),
    path('contact', contact, name="contact"),
    path('login', login, name="login"),
    path('profile', profile, name="profile"),
    path('register', register, name="register"),
]