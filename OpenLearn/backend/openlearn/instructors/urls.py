from django.urls import path
from .views import InstructorListView, InstructorDetailView, CourseListView, CourseDetailView,CourseViewSet

urlpatterns = [
    path('instructors/', InstructorListView.as_view(), name='instructor-list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/addcourse/',CourseViewSet.as_view({'post': 'create'}),name='add-course')
]
