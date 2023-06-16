from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        seri = StudentSerializers(data = pydata)
        if seri.is_valid():
            seri.save()
            res = {'msg':'data created'}
            return JsonResponse(seri.data)
        return JsonResponse(seri.errors)