from rest_framework import serializers
from todolistApp.models import Staff,TasksProfesionnel,Projects,Comptes,TasksPersonal

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ('id',
                'type',
                'mail',
                'password')

class TasksProfessionnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksProfesionnel
        fields = ['id', 'name', 'date','completed' , 'users', 'projectID']
        
class TasksPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksPersonal
        fields = ['id', 'name', 'date', 'completed', 'projectID']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name','type','staffID']

class ComptesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comptes
        fields = ['id', 'name', 'twitter', 'gethub', 'linkedin', 'adress', 'tel','image','staffID']

                
        