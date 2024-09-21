from rest_framework import generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from .models import Course
from instructors.models import InstructorProfile


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        """
        Optionally filters the courses based on query parameters from the request.
        """
        queryset = Course.objects.all()
        level = self.request.query_params.get('level', None)
        language = self.request.query_params.get('language', None)
        duration = self.request.query_params.get('duration', None)

        # Apply filters if the parameters exist
        if level:
            queryset = queryset.filter(level=level)
        if language:
            queryset = queryset.filter(language=language)
        if duration:
            # Assuming `duration` is a string like '1-4 weeks', you'll need to translate that into a numeric range.
            if duration == "1-4 weeks":
                queryset = queryset.filter(duration__lte=4)
            elif duration == "4-8 weeks":
                queryset = queryset.filter(duration__gt=4, duration__lte=8)
            elif duration == "8+ weeks":
                queryset = queryset.filter(duration__gt=8)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        instructor_email = request.data.get('instructor_email')  # Get the instructor email from request

        # Look up the instructor profile by email
        instructor_profile = get_object_or_404(InstructorProfile, user__email=instructor_email)

        # Create the course object with the instructor
        course = Course(
            title=request.data['title'],
            description=request.data['description'],
            duration=request.data['duration'],
            level=request.data['level'],
            language=request.data['language'],
            syllabus=request.data['syllabus'],
            instructor=instructor_profile  # Set the instructor using the profile
        )
        course.save()  # Save the course instance
        serializer = self.get_serializer(course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)