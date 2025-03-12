from django import forms
from .models import CourseModel, TaskModel, ProfileModel, BookingModel

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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    phone = forms.CharField(min_length=10 ,max_length=10)

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date.weekday() in [5,6]:
            raise forms.ValidationError("Cannot book on weekends")
        return date
    
def validate_name(name):
    if any(filter(lambda n: n.isdigit(), name)):
        raise forms.ValidationError("Name should not contain digits")
    return name

def validate_message(message):
    if len(message) < 20:
        raise forms.ValidationError("Message should have atleast 20 characters")
    return message

class FeedbackFormValidation(forms.Form):
    name = forms.CharField(max_length=50, validators=[validate_name])
    message = forms.CharField(validators=[validate_message])

class ProfileFormRedirect(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()