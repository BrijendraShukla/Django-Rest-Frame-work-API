from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            seri = StudentSerializers(stu)
            return Response(seri.data)
        stu = Student.objects.all()
        seri = StudentSerializers(stu, many=True)
        return Response(seri.data )
    
    if request.method == 'POST':
        data = request.data
        seri = StudentSerializers(data = data)
        if seri.is_valid():
            seri.save()
            return Response({'msg':'data created'})
        return Response(seri.errors)
    
    if request.method == 'PUT':
        data = request.data
        id = data.get('id')
        stu = Student.objects.get(pk=id)
        seri = StudentSerializers(stu, data = data, partial = True)
        if seri.is_valid():
            seri.save()
            return Response({'msg':'data updated'})
        return Response(seri.errors)
    
    if request.method == 'DELETE':
        data = request.data
        id = data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})