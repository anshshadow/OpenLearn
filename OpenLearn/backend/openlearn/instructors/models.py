from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class InstructorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='instructor_pictures/', blank=True, null=True)
    qualifications = models.TextField()
    experience = models.IntegerField(help_text="Years of experience")
    social_links = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, related_name='courses')
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    category=models.CharField(max_length=50,default='web development')
    price=models.FloatField(default=10000)
    syllabus = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
