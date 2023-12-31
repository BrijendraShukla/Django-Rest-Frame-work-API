from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=150)
    roll = serializers.IntegerField()

    def create(self,validate_data):
        return Student.objects.create(**validate_data)