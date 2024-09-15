# student/models.py
from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrolled_courses = models.ManyToManyField('courses.Course', related_name='students', blank=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
