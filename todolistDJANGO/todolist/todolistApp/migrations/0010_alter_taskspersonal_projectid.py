# Generated by Django 4.2.9 on 2024-02-09 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0009_taskspersonal_projectid_alter_projects_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskspersonal',
            name='projectID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolistApp.projects'),
        ),
    ]