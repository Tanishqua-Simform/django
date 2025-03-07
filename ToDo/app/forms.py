from django import forms
from django.utils.timezone import now

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

