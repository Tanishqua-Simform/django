"""
URL configuration for Hello_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from Greetings import views as g
# from Profile import views as p

# # Method - 1: With urls of all apps together
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', g.home, name='greet_home'),
#     path('tani/', g.tani, name='greet_tani'),
#     path('soham/', g.soham, name='greet_soham'),
#     path('lamha/', g.lamha, name='greet_lamha'),
#     path('profile/', p.home, name='profile_home'),
#     path('profile/tani/', p.tani, name='profile_tani'),
#     path('profile/soham/', p.soham, name='profile_soham'),
#     path('profile/lamha/', p.lamha, name='profile_lamha'),
# ]


# Method - 2: Integrating URLs from different apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', include('Greetings.urls')),
    path('profile/', include('Profile.urls'))
]

