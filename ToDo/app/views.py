from django.shortcuts import render
from app.models import todo_list
from app.forms import CreateTask

def my_todos(request):
    tasks = todo_list.read_all(todo_list)
    return render(request, 'app/my_todos.html', {'todo_list': tasks})

def pending_todos(request):
    tasks = todo_list.read_pending(todo_list)
    return render(request, 'app/pending_todos.html', {'todo_list': tasks})

def details(request, task_id):
    task = todo_list.read_task(todo_list, task_id)
    return render(request, 'app/details.html', {'task': task})

def create_todo(request):
    fm = CreateTask()
    return render(request, 'app/create_todo.html', {'form': fm})

def update_todo(request, task_id):
    fm = CreateTask()
    task = todo_list.read_task(todo_list, task_id)
    return render(request, 'app/update_todo.html', {'form': fm, 'task': task})