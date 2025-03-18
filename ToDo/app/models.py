from django.db import models
from django.contrib.auth.models import User, Group

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
    assigned_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_to=models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_tasks', limit_choices_to={'groups__name':'Mentee'})
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def read_all(cls, user_id):
        return cls.objects.filter(assigned_to=user_id)
    
    def read_pending(cls, user_id):
        return cls.objects.filter(status='pending', assigned_to=user_id)
    
    def read_completed(cls, user_id):
        return cls.objects.filter(status='completed', assigned_to=user_id)
    
    def read_task(cls, task_id):
        return cls.objects.filter(id=task_id).first()

class ProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='profile_pics/')

    def save(self, *args, **kwargs):
        if self.photo:
            img_name = f'{self.user}.png'
            self.photo.save(img_name, content=self.photo, save=False)
        super().save(*args, **kwargs)