# Generated by Django 3.0.2 on 2020-01-27 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListfOfBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('current_page', models.IntegerField()),
                ('total_pages', models.IntegerField()),
                ('list_of_books', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='app.ListfOfBooks')),
            ],
        ),
    ]
