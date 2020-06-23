from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    distributor = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title