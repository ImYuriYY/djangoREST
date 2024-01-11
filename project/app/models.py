from django.db import models
from datetime import date

class Book(models.Model):
    name = models.CharField(max_length=200)
    annotation = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    public_year = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
