from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    priority_choice = (
        ('high', 'High'),
        ('low', 'Low'),
        ('medium', 'Medium')
    )
    status_choice = (
        ('pending', 'Pending'),
        ('completed', 'Completed')
    )
    title=models.CharField(max_length=100)
    description=models.TextField()
    due_date=models.DateField()
    priority=models.CharField(max_length=6, choices=priority_choice)
    status=models.CharField(max_length=9, choices=status_choice)
    assigned_by=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def read_all(cls):
        return cls.objects.all()
    
    def read_pending(cls):
        return cls.objects.filter(status='pending')
    
    def read_completed(cls):
        return cls.objects.filter(status='completed')
    
    def read_task(cls, task_id):
        return cls.objects.filter(id=task_id).first()

class ProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/profile_pics/')