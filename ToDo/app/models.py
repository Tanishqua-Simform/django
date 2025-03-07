from django.db import models

class todo_list(models.Model):
    title=models.CharField(max_length=10)
    description=models.TextField()
    due_date=models.DateField()
    priority=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    assigned_by=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def read_all(cls):
        return cls.objects.all()
    
    def read_pending(cls):
        return cls.objects.filter(status='Pending')
    
    def read_task(cls, task_id):
        return cls.objects.filter(id=task_id).first()