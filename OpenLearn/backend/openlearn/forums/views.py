from rest_framework import viewsets
from .models import ForumThread, ForumPost
from .serializers import ForumThreadSerializer, ForumPostSerializer

class ForumThreadViewSet(viewsets.ModelViewSet):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer

class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
