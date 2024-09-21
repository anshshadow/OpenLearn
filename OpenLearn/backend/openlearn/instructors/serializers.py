from rest_framework import serializers
from .models import InstructorProfile, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        

class InstructorProfileSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = InstructorProfile
        fields = '__all__'
