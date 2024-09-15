# student/views.py
from rest_framework import generics
from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentProfileView(generics.RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
