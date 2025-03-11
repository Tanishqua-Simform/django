from django import forms
from .models import CourseModel, TaskModel, ProfileModel

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea())

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = "__all__"

def validate_username(username):
    if len(username) >= 5:
        return username
    raise forms.ValidationError("Username should be of atleast 5 characters")

def validate_email(email):
    if email.endswith('.com'):
        return email
    raise forms.ValidationError("Email should end with .com")

def validate_password(password):
    if len(password) >= 8:
        return password
    raise forms.ValidationError("password should be of atleast 8 characters")


class ValidateForm(forms.Form):
    username = forms.CharField(validators=[validate_username])
    email = forms.EmailField(validators=[validate_email])
    password = forms.CharField(validators=[validate_password])

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input-box"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter password"}))

TaskFormset = forms.modelformset_factory(TaskModel, fields=('title', 'status'), extra=1)

class ProfileManual(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'