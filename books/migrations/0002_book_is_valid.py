# Generated by Django 5.0 on 2024-01-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]
