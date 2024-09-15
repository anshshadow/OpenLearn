# student/urls.py
from django.urls import path
from .views import StudentProfileView

urlpatterns = [
    path('profile/<int:pk>/', StudentProfileView.as_view(), name='student-profile'),
]
