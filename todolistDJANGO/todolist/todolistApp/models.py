from django.db import models
from django.utils import timezone

class Staff(models.Model):
    id = models.AutoField(primary_key=True, default=None)  # Ajout de default=None
    mail = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True, null=True, default='')
    password = models.CharField(max_length=10)

class TasksProfesionnel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False) 
    users=models.CharField(max_length=100,default='')
    projectID = models.ForeignKey("Projects", on_delete=models.CASCADE, null=True)
    

class TasksPersonal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False) 
    projectID = models.ForeignKey("Projects", on_delete=models.CASCADE, null=True)
    
class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='')
    staffID = models.ForeignKey("Staff",on_delete=models.CASCADE, null=True)

    

class Comptes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default=' ')
    twitter = models.CharField(max_length=100,default=' ')
    gethub = models.CharField(max_length=100,default=' ')
    linkedin = models.CharField(max_length=100,default=' ')
    adress = models.CharField(max_length=100,default=' ')
    tel = models.IntegerField(null=True)
    image = models.ImageField(blank=True, default='imagemohamed.png')    
    staffID = models.ForeignKey("Staff",on_delete=models.CASCADE, null=True)

    
