# Generated by Django 3.0.2 on 2020-01-11 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='biopic',
        ),
    ]