from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(verbose_name="Created at")
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()
    is_valid = models.BooleanField(default=True)
    libraries = models.ManyToManyField(
        'library.Library', related_name='books', blank=True)

    def __str__(self):
        return self.title
