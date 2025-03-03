from django.urls import path
from Greetings.views import home, tani, soham, lamha

urlpatterns = [
    path('', home, name='greet_home'),
    path('tani/', tani, name='greet_tani'),
    path('soham/', soham, name='greet_soham'),
    path('lamha/', lamha, name='greet_lamha'),
]
