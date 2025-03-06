from django.shortcuts import render
from app.models import todo_list

def all_todo(request):
    tasks = todo_list.read_all(todo_list)
    return render(request, 'app/all_todo.html', {'todo_list': tasks})

def pending_todo(request):
    tasks = todo_list.read_pending(todo_list)
    return render(request, 'app/all_todo.html', {'todo_list': tasks})
