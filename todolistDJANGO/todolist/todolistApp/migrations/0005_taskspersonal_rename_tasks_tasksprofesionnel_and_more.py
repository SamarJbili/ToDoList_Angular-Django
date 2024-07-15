# Generated by Django 4.2.9 on 2024-02-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0004_rename_compteadress_comptes_adress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksPersonal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Tasks',
            new_name='TasksProfesionnel',
        ),
        migrations.AlterField(
            model_name='staff',
            name='type',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
