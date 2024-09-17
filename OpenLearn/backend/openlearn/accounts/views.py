from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
import datetime
from students.models import StudentProfile
from instructors.models import InstructorProfile
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class UserProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        email1 = request.query_params.get('username1') 
        print(email1)
        user=User.objects.get(email='12345@gmail.com')
        
        # Assuming you have a serializer for the User model to format the response
        user_data = {
            'username': user.username,
            'email': user.email,
            'role': user.role,  # Assuming 'role' is a field in the User model
        }

        # Fetch additional profile data based on the user's role
        if user.role == 'student':
            try:
                student_profile = StudentProfile.objects.get(user=user)
                user_data['profile'] = {
                    'enrolled_courses': [enrolled_courses.title for enrolled_courses in student_profile.enrolled_courses.all()]
                }
            except StudentProfile.DoesNotExist:
                user_data['profile'] = 'No student profile found'

        elif user.role == 'instructor':
            try:
                instructor_profile = InstructorProfile.objects.get(user=user)
                user_data['profile'] = {
                    'teaching_courses': [course.title for course in instructor_profile.courses.all()],
                    'experience': instructor_profile.experience,  # Assuming an experience field exists
                }
            except InstructorProfile.DoesNotExist:
                user_data['profile'] = 'No instructor profile found'

        # Return the user data
        return Response(user_data)

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role', 'student')  # Default to 'student' if not provided

        if User.objects.filter(username=username).exists():
            return Response({'detail': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'detail': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password, role=role)
        user.save()

        # Create a student or instructor profile based on the role
        if role == 'student':
            StudentProfile.objects.create(user=user)
        elif role == 'instructor':
            InstructorProfile.objects.create(user=user)

        return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        if user is None:
            raise AuthenticationFailed('Invalid credentials')

        payload = {
            'id': user.id,
            'exp': timezone.now() + datetime.timedelta(minutes=60),
            'iat': timezone.now(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token)
        response.data = {
            'token': token,
            'role': user.role
        }
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'Logout successful'}
        return response
