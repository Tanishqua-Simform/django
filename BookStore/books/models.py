from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    