# Generated by Django 3.2.9 on 2021-12-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0004_alter_task_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.TextField(choices=[('later', 'Later'), ('doing', 'Doing'), ('done', 'Done')], max_length=8),
        ),
    ]
