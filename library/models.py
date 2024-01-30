from django.db import models
from books.models import Book


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def available_books(self):
        return Book.objects.filter(libraries=self, is_valid=True)


class FileModel(models.Model):
    files = models.FileField(upload_to='upload/')
