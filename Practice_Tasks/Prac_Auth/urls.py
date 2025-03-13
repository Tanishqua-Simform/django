from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from .views import register, login_form, home, dashboard, logout_form, profile

urlpatterns = [
    path('home', home, name="home"),
    path('register', register, name="register"),
    path('login', login_form, name="auth_login"),
    path('change-password', PasswordChangeView.as_view(template_name='Prac_Auth/password-change.html', success_url='dashboard'), name="change_password"),
    path('dashboard', dashboard, name="auth_dashboard"),
    path('profile', profile, name="auth_profile"),
    path('logout', logout_form, name="auth_logout"),
]
