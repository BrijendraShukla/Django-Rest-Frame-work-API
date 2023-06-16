from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None :
            stu = Student.objects.get(id=id)
            seri = StudentSerializers(stu)
            return JsonResponse(seri.data)
        stu = Student.objects.all()
        seri = StudentSerializers(stu , many = True)
        return JsonResponse(seri.data,safe=False)
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seri = StudentSerializers(data = pythondata)
        if seri.is_valid():
            seri.save()
            res = {'msg':'data created'}
            return JsonResponse(res)
        return JsonResponse(seri.errors)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        seri = StudentSerializers(stu, data = pythondata, partial = True)
        if seri.is_valid():
            seri.save()
            res = {'msg':'data updated'}
            return JsonResponse(res)
        return JsonResponse(seri.errors)
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}
        return JsonResponse(res, safe=False)