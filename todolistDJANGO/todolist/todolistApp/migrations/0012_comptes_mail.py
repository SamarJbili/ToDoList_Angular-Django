# Generated by Django 4.2.9 on 2024-02-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0011_projects_mail_alter_staff_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='comptes',
            name='mail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='todolistApp.staff'),
        ),
    ]
