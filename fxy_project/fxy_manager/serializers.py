from rest_framework import serializers,viewsets
from .models import student_info

class student_info_serializer(serializers.ModelSerializer):
    class Meta:
        model=student_info
        fields=("__all__")