from django.db import models

class todo_list(models.Model):
    task=models.CharField(max_length=100)
    status=models.CharField(max_length=10)
    assigned_by=models.CharField(max_length=20)

    def __str__(self):
        return self.status
    
    def read_all(cls):
        return cls.objects.all()
    
    def read_pending(cls):
        return cls.objects.filter(status='Pending')