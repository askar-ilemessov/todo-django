# Generated by Django 3.2.9 on 2021-12-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_alter_task_task_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.TextField(blank=True, choices=[('Later', 'Later'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=8),
        ),
    ]
