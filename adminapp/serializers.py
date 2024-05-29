from rest_framework import serializers
from .models import Department,Service

class deptserializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
class loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
