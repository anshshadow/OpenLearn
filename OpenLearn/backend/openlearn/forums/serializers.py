# forums/serializers.py

from rest_framework import serializers
from .models import ForumThread, ForumPost

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id', 'author', 'content', 'created_at']

class ForumThreadSerializer(serializers.ModelSerializer):
    posts = ForumPostSerializer(many=True, read_only=True)

    class Meta:
        model = ForumThread
        fields = ['id', 'title', 'author', 'created_at', 'updated_at', 'is_for_instructors', 'posts']
