# Generated by Django 5.0.6 on 2024-07-19 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('task_management', 'Can create, assign and delete tasks')]},
        ),
    ]