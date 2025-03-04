from django.urls import path
from Profile.views import home, tani, soham, lamha, show_posts, show_likes, show_details

urlpatterns = [
    path('', home, name='greet_home'),
    path('tani/', tani, name='greet_tani'),
    path('soham/', soham, name='greet_soham'),
    path('lamha/', lamha, name='greet_lamha'),
    path('posts/', show_posts, name='show_posts'),
    path('likes/', show_likes, name='show_likes'),
    path('details/', show_details, name='show_details'),
]
