from todolistApp.models import Staff, Projects, Comptes, TasksProfesionnel,TasksPersonal
from todolistApp.serializers import StaffSerializer, ProjectsSerializer, ComptesSerializer, TasksProfessionnelSerializer,TasksPersonalSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.views.decorators.http import require_GET

@csrf_exempt
def staff_api(request, staff_id=None):
    if request.method == 'GET':
        if staff_id:
            try:
                staff_member = Staff.objects.get(id=staff_id)
                serializer = StaffSerializer(staff_member)
                return JsonResponse(serializer.data, safe=False)
            except ObjectDoesNotExist:
                return JsonResponse("Staff member does not exist.", status=404)
        else:
            staff_members = Staff.objects.all()
            serializer = StaffSerializer(staff_members, many=True)
            return JsonResponse(serializer.data, safe=False)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StaffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'PUT':
        if staff_id:
            data = JSONParser().parse(request)
            try:
                staff_member = Staff.objects.get(id=staff_id)
                serializer = StaffSerializer(staff_member, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({"message": "Updated Successfully!!"})
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                return JsonResponse({"error": "Staff member does not exist."}, status=404)
        else:
            return JsonResponse({"error": "Staff ID is required for update."}, status=400)
    
    elif request.method == 'DELETE':
        if staff_id:
            try:
                staff_member = Staff.objects.get(id=staff_id)
                staff_member.delete()
                return JsonResponse("Deleted Successfully!!", safe=False)
            except ObjectDoesNotExist:
                return JsonResponse("Staff member does not exist.", status=404)
        else:
            return JsonResponse("Staff ID is required for deletion.", status=400)
        

@csrf_exempt
def projects_api(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                project = Projects.objects.get(id=id)
                serializer = ProjectsSerializer(project)
                return JsonResponse(serializer.data)
            except Projects.DoesNotExist:
                return JsonResponse({'error': 'Project not found'}, status=404)
        else:
            projects = Projects.objects.all()
            serializer = ProjectsSerializer(projects, many=True)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        try:
            project = Projects.objects.get(id=id)
            data = JSONParser().parse(request)
            serializer = ProjectsSerializer(project, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except Projects.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)
    elif request.method == 'DELETE':
        try:
            project = Projects.objects.get(id=id)
            project.delete()
            return JsonResponse({'message': 'Project deleted successfully'})
        except Projects.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
@csrf_exempt
def comptes_api(request, id=0):
    if request.method == 'GET':
        comptes_list = Comptes.objects.all()
        serializer = ComptesSerializer(comptes_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComptesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        compte_id = id
        if compte_id is not None:
            try:
                compte = Comptes.objects.get(id=compte_id)
                serializer = ComptesSerializer(compte, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("Updated Successfully!!", safe=False)
                return JsonResponse(serializer.errors, status=400)
            except Comptes.DoesNotExist:
                return JsonResponse("Compte does not exist.", status=404)
        else:
            return JsonResponse("Compte ID is missing in request data.", status=400)

    elif request.method == 'DELETE':
        try:
            compte = Comptes.objects.get(id=id)
            compte.delete()
            return JsonResponse("Deleted Successfully!!", safe=False)
        except Comptes.DoesNotExist:
            return JsonResponse("Compte does not exist.", status=404)

@csrf_exempt
def tasksPro_api(request, id=0):
    if request.method == 'GET':
        tasks = TasksProfesionnel.objects.all()
        serializer = TasksProfessionnelSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TasksProfessionnelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully!!", safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        task_id = data.get('id')
        if task_id is not None:
            try:
                task = TasksProfesionnel.objects.get(id=task_id)
                serializer = TasksProfessionnelSerializer(task, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("Updated Successfully!!", safe=False)
                return JsonResponse(serializer.errors, status=400)
            except TasksProfesionnel.DoesNotExist:
                return JsonResponse({"error": "Task does not exist."}, status=404)
        else:
            return JsonResponse({"error": "Task id not provided."}, safe=False, status=400)

    elif request.method == 'DELETE':
        try:
            task = TasksProfesionnel.objects.get(id=id)
            task.delete()
            return JsonResponse({"message": "Deleted Successfully!!"})
        except TasksProfesionnel.DoesNotExist:
            return JsonResponse({"error": "Task does not exist."}, status=404)

@csrf_exempt
def tasksPers_api(request, id=0):
    if request.method == 'GET':
        tasks = TasksPersonal.objects.all()
        serializer = TasksPersonalSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TasksPersonalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully!!", safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        task_id = data.get('id')
        if task_id is not None:
            try:
                task = TasksPersonal.objects.get(id=task_id)
                serializer = TasksPersonalSerializer(task, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("Updated Successfully!!", safe=False)
                return JsonResponse(serializer.errors, status=400)
            except TasksPersonal.DoesNotExist:
                return JsonResponse({"error": "Task does not exist."}, status=404)
        else:
            return JsonResponse({"error": "Task id not provided."}, safe=False, status=400)

    elif request.method == 'DELETE':
        try:
            task = TasksPersonal.objects.get(id=id)
            task.delete()
            return JsonResponse({"message": "Deleted Successfully!!"})
        except TasksPersonal.DoesNotExist:
            return JsonResponse({"error": "Task does not exist."}, status=404)

@csrf_exempt
def save_file(request):
    if request.method == 'POST' and request.FILES.get('uploadedFile'):
        file = request.FILES['uploadedFile']
        file_name = default_storage.save(file.name, file)
        return JsonResponse(file_name, safe=False)
    else:
        return JsonResponse("Failed to upload file. Please make sure to use POST method and provide a file.", status=400)
