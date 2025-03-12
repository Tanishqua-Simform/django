from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from .views import register, login_form, home, dashboard, logout_form

urlpatterns = [
    path('register', register, name="register"),
    path('login', login_form, name="auth-login"),
    path('logout', logout_form, name="auth-logout"),
    path('change-password', PasswordChangeView.as_view(template_name='Prac_Auth/password-change.html'), name="auth-login"),
    path('home', home, name="home"),
    path('dashboard', dashboard, name="auth-dashboard"),
]
