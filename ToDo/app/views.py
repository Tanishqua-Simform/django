from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from app.models import TodoList, ProfilePhoto
from app.forms import CreateTask, CreateTaskModel, RegisterUser, LoginUser, ProfileForm
from app.signals import email_signal

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
    user = User.objects.get(username=request.user)
    tasks = TodoList.read_all(TodoList, user.id)
    if request.method=='POST':
        search = request.POST['search']
        data = tasks.filter(Q(title__icontains=search)| Q(priority__istartswith=search) | Q(status__istartswith=search))
        if not data:
            messages.error(request, 'Oops No data available!', extra_tags='danger')
        return render(request, 'app/my_todos.html', {'todo_list': data, 'search': True})
    return render(request, 'app/my_todos.html', {'todo_list': tasks, 'search': True})

@login_required(login_url='login')
def pending_todos(request):
    user = User.objects.get(username=request.user)
    tasks = TodoList.read_pending(TodoList, user.id)
    return render(request, 'app/pending_todos.html', {'todo_list': tasks})

@login_required(login_url='login')
def completed_todos(request):
    user = User.objects.get(username=request.user)
    tasks = TodoList.read_completed(TodoList, user.id)
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
        user = User.objects.get(username=request.user)
        data = request.POST.copy()
        data['assigned_by'] = user.id
        form = CreateTaskModel(data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Created successfully!')
            subject = 'New Task Created!'
            receiver = User.objects.get(id=request.POST['assigned_to'])
            to_email = [receiver.email]
            message = f"Hello {receiver.username}, New task Created by {user.username}"
            email_signal.send(sender=None, subject=subject, message=message , to_email=to_email)
            return redirect(reverse('assigned'))
    fm = CreateTaskModel()
    return render(request, 'app/create_todo.html', {'form': fm})


@login_required(login_url='login')
def update_todo(request, task_id):
    task = TodoList.read_task(TodoList, task_id)
    if request.method == 'POST':
        # form = CreateTaskModel(request.POST)
        user = User.objects.get(username=request.user)
        form = CreateTaskModel(request.POST, instance=task)
        if form.is_valid():
            # task.title = request.POST['title']
            # task.description = request.POST['description']
            # task.due_date = request.POST['due_date']
            # task.priority = request.POST['priority']
            # task.status = request.POST['status']
            # task.assigned_by = request.POST['assigned_by']
            # task.save()

            form.save()
            messages.success(request, 'Task Updated successfully!', extra_tags='warning')
            subject = 'Old Task Updated!'
            receiver = User.objects.get(id=request.POST['assigned_to'])
            to_email = [receiver.email]
            message = f"Hello {receiver.username}, Previous task was Updated by {user.username}"
            email_signal.send(sender=None, subject=subject, message=message , to_email=to_email)
            return redirect(reverse('assigned'))
    fm = CreateTaskModel(instance=task)
    return render(request, 'app/update_todo.html', {'form': fm})

@login_required(login_url='login')
def delete_todo(request, task_id):
    task = TodoList.read_task(TodoList, task_id)
    assigned_to = task.assigned_to
    task.delete()
    messages.error(request, 'Task Deleted successfully!', extra_tags='danger')
    user = User.objects.get(username=request.user)
    subject = 'Task Deleted!'
    receiver = User.objects.get(id=assigned_to.id)
    to_email = [receiver.email]
    message = f"Hello {receiver.username}, Task was Deleted by {user.username}"
    email_signal.send(sender=None, subject=subject, message=message , to_email=to_email)
    return redirect(reverse('assigned'))

@login_required(login_url='login')
def upload_profile(request):
    user = User.objects.get(username=request.user)
    profile_obj = ProfilePhoto.objects.filter(user_id=user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if profile_obj:
                profile_obj.name = request.POST['name']
                profile_obj.photo = request.FILES['photo']
                profile_obj.save()
            else:
                form.save()
            messages.success(request, 'Profile added successfully!')
            return redirect(reverse('show_profile'))
        else:
            messages.error(request, 'Error Occured!', extra_tags='danger')
    form = ProfileForm(data={'user':request.user})
    return render(request, 'app/upload_profile.html', {'form': form})

@login_required(login_url='login')
def show_profile(request):
    user = User.objects.get(username=request.user)
    profile_obj = ProfilePhoto.objects.filter(user_id=user.id).first()
    if profile_obj:
        path = f'/media/{profile_obj.photo}'
        name = profile_obj.name
    else:
        path='/media/profile_pics/no_profile.png'
        name='Anonymous User'
    return render(request, 'app/profile.html', {'path': path, 'name': name})

def is_mentor(user):
    return user.groups.filter(name='Mentor').exists()

@login_required(login_url='login')
@user_passes_test(is_mentor, login_url='my_todos')
def assigned(request):
    user = User.objects.get(username=request.user)
    tasks = TodoList.objects.filter(assigned_by=user.id)
    return render(request, 'app/assigned.html', {'todo_list': tasks})