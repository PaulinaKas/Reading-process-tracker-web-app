# Generated by Django 3.0.2 on 2020-01-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_listfofbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='list_of_books',
            field=models.TextField(default=''),
        ),
    ]
