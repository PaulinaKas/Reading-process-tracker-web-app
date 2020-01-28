# Generated by Django 3.0.2 on 2020-01-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200128_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('list_of_books', 'title')},
        ),
    ]
