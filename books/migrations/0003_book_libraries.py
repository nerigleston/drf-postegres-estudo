# Generated by Django 5.0 on 2024-01-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_is_valid'),
        ('library', '0002_remove_library_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='libraries',
            field=models.ManyToManyField(blank=True, related_name='books', to='library.library'),
        ),
    ]
