from django import forms
from django.utils.timezone import now
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoList, ProfilePhoto

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUser(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class CreateTask(forms.Form):
    priorities = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title=forms.CharField(max_length=10)
    description=forms.CharField(widget=forms.Textarea())
    due_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=now())
    priority=forms.ChoiceField(choices=priorities)
    status=forms.CharField()
    assigned_by=forms.CharField()

class CreateTaskModel(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfilePhoto
        fields = '__all__'
        # fields = ['name', 'photo']