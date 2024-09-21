from rest_framework import viewsets
from .models import ForumThread, ForumPost
from .serializers import ForumThreadSerializer, ForumPostSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
class ForumThreadViewSet(viewsets.ModelViewSet):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerializer

class ForumPostViewSet(viewsets.ModelViewSet):
    serializer_class = ForumPostSerializer

    def get_queryset(self):
        thread_id = self.request.query_params.get('thread_id', None)
        if thread_id is not None:
            return ForumPost.objects.filter(thread_id=thread_id)
        return ForumPost.objects.all()
    
    def create(self, request, *args, **kwargs):
        # Get thread_id from the request data
        thread_id = request.data.get('thread_id', None)
        
        # Validate that thread_id is provided
        if not thread_id:
            return Response({'error': 'thread_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate that the thread exists
        thread = get_object_or_404(ForumThread, id=thread_id)

        # Use the serializer to validate and save the post
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(thread=thread)  # Save the post and associate it with the thread
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
