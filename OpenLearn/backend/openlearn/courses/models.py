from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
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

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.title
