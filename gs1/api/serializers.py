from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=150)
    roll = serializers.IntegerField()