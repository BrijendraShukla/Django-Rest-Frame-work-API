from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

### for specific data 
def student_details(request,pk):
    stu = Student.objects.get(id=pk) ### complex data stored into database 
    serializer = StudentSerializers(stu) ###  complex data converted into object or python 
    return JsonResponse(serializer.data) ### python data to JSON data so that front end can understand
    # json_data = JSONRenderer().render(serializer.data) 
    # return HttpResponse(json_data, content_type = 'application/json')

### for all set of data pr Query set
def student_details_all(request):
    students = Student.objects.all()
    seri = StudentSerializers(students,many=True)
    json_data = JSONRenderer().render(seri.data)
    return HttpResponse(json_data, content_type ='application/json')
    # return JsonResponse(seri.data,safe=False)