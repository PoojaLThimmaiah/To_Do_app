# Generated by Django 3.1.1 on 2020-10-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='completed',
            field=models.BooleanField(),
        ),
    ]