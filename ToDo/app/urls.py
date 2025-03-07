from django.urls import path
from app.views import my_todos, pending_todos, details, create_todo, update_todo

urlpatterns = [
    path('', my_todos, name='my_todos'),
    path('pending/', pending_todos, name='pending_todos'),
    path('details/<int:task_id>', details, name='details'),
    path('create/', create_todo, name='create_todo'),
    path('update/<int:task_id>', update_todo, name='update_todo'),
]