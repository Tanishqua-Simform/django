from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import LoginModel

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'class': 'col-lg-4 mx-auto mt-5'}
        self.helper.layout = Layout(
            Field('name', css_class='text-primary'),
            Field('email', css_class='text-success'),
            Field('phone', css_class='text-danger'),
            Field('message', css_class='text-warning'),
        )
        self.helper.add_input(Submit('submit', 'Send Message'))

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ['username', 'password']

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    bio = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'class': 'col-lg-4 mx-auto mt-5'}
        self.helper.add_input(Submit('submit', 'Send Message'))

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'class': 'col-lg-4 mx-auto mt-5'}
        self.helper.add_input(Submit('submit', 'Register'))

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data['password']
        p2 = cleaned_data['confirm_password']

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords don't match!")
        return cleaned_data
