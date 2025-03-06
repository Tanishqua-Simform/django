from django.urls import path
from app.views import all_todo, pending_todo

urlpatterns = [
    path('', all_todo, name='todo_list'),
    path('pending/', pending_todo, name='pending_todo')
]