from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm, CourseForm, ValidateForm, LoginForm, TaskFormset, ProfileManual
from .models import TaskModel

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            html = f'<h1>Name: {name}</h1> {email} <h4>Feedback: {feedback}</h4>'
            return HttpResponse(html)
    else:
        form = FeedbackForm()
    return render(request, 'Prac_Form/feedback.html', {'form': form})

def course_modelform(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Course created successfully!")
    else:
        form = CourseForm()
    return render(request, "Prac_Form/create_course.html", {'form': form})

def form_validation(request):
    if request.method == "POST":
        form = ValidateForm(request.POST)
        if form.is_valid():
            return HttpResponse("The Form Contains Validated Data!")
    else:
        form = ValidateForm()
    return render(request, "Prac_Form/validate.html", {'form': form})

def login_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Logged In Successfully")
    else:
        form = LoginForm()
    return render(request, "Prac_Form/login.html", {'form': form})


def task_formset(request):
    formset = TaskFormset(queryset=TaskModel.objects.all())
    if request.method == "POST":
        formset = TaskFormset(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse("Multiple Data Inserted using Formset")
    return render(request, "Prac_Form/create_task.html", {'formset': formset})

def profile_manual(request):
    if request.method == "POST":
        form = ProfileManual(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.age += 1
            profile.save()
            return HttpResponse("Profile Created!")
    else:
        form = ProfileManual()
    return render(request, "Prac_Form/create_profile.html", {'form': form})
    