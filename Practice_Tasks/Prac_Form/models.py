from django.db import models

class CourseModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()

class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    status= models.CharField(max_length=10)

class ProfileModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class BookingModel(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()