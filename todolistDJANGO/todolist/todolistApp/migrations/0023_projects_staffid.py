# Generated by Django 5.0.3 on 2024-03-18 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0022_remove_projects_staffid'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='staffID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolistApp.staff'),
        ),
    ]
