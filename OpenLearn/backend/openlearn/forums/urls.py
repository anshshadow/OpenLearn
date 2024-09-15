from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ForumThreadViewSet, ForumPostViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'threads', ForumThreadViewSet, basename='forumthread')
router.register(r'posts', ForumPostViewSet, basename='forumpost')

# Include the router's URLs in your urlpatterns
urlpatterns = [
    path('api/', include(router.urls)),
]
