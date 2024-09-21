from rest_framework import generics,viewsets,status
from .models import InstructorProfile, Course
from .serializers import InstructorProfileSerializer, CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class InstructorListView(generics.ListCreateAPIView):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer