# Generated by Django 4.2.9 on 2024-02-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0017_remove_tasksprofesionnel_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksprofesionnel',
            name='users',
            field=models.CharField(default='', max_length=100),
        ),
    ]
