from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import TodoList
from app.forms import CreateTask, CreateTaskModel, RegisterUser, LoginUser, ProfileForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully!')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Incorrect data entered!', extra_tags='danger')
    form = RegisterUser()
    return render(request, 'app/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, username=un, password=pw)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect(reverse('my_todos'))
        else:
            messages.error(request, 'Incorrect credentials!', extra_tags='danger')
    form = LoginUser()
    return render(request, 'app/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect(reverse('login'))

@login_required(login_url='login')
def my_todos(request):
    tasks = TodoList.read_all(TodoList)
    return render(request, 'app/my_todos.html', {'todo_list': tasks})

@login_required(login_url='login')
def pending_todos(request):
    tasks = TodoList.read_pending(TodoList)
    return render(request, 'app/pending_todos.html', {'todo_list': tasks})

@login_required(login_url='login')
def completed_todos(request):
    tasks = TodoList.read_completed(TodoList)
    return render(request, 'app/pending_todos.html', {'todo_list': tasks})

@login_required(login_url='login')
def details(request, task_id):
    task = TodoList.read_task(TodoList, task_id)
    return render(request, 'app/details.html', {'task': task})

@login_required(login_url='login')
def create_todo(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        html = f'Form Submitted Successfully with below data - \n{form}'
        return HttpResponse(html)
    fm = CreateTask()
    return render(request, 'app/create_todo.html', {'form': fm})

@login_required(login_url='login')
def create_todo_model(request):
    if request.method == 'POST':
        form = CreateTaskModel(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Created successfully!')
            return redirect(reverse('my_todos'))
    fm = CreateTaskModel()
    return render(request, 'app/create_todo.html', {'form': fm})


@login_required(login_url='login')
def update_todo(request, task_id):
    task = TodoList.read_task(TodoList, task_id)
    if request.method == 'POST':
        # form = CreateTaskModel(request.POST)
        form = CreateTaskModel(request.POST, instance=task)
        if form.is_valid():
            # task.title = request.POST['title']
            # task.description = request.POST['description']
            # task.due_date = request.POST['due_date']
            # task.priority = request.POST['priority']
            # task.status = request.POST['status']
            # task.assigned_by = request.POST['assigned_by']
            # task.save()

            messages.success(request, 'Task Updated successfully!', extra_tags='warning')
            form.save()
            return redirect(reverse('my_todos'))
    fm = CreateTaskModel(instance=task)
    return render(request, 'app/update_todo.html', {'form': fm})

@login_required(login_url='login')
def delete_todo(request, task_id):
    task = TodoList.read_task(TodoList, task_id)
    task.delete()
    messages.error(request, 'Task Deleted successfully!', extra_tags='danger')
    return redirect(reverse('my_todos'))

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile added successfully!')
            # return redirect(reverse(f'show_profile/{request.POST}'))
        else:
            messages.error(request, 'Error Occured!', extra_tags='danger')
    form = ProfileForm()
    return render(request, 'app/profile.html', {'form': form})

def show_profile(request, user):
    pass
    # photo = 'media/profile_'
    # return render(request, 'app/profile.html', {'form': form})
    # To be implemented next