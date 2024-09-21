from django.urls import path
from .views import CourseListView, CourseDetailView, LessonListView, LessonDetailView,CourseViewSet

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('courses/addcourse/',CourseViewSet.as_view({'post': 'create'}),name='add-course')
]
