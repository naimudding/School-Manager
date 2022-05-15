from rest_framework import serializers
from .models import Students

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'sr_no', 'fullname', 'guardian_name', 'class_name', 'status']