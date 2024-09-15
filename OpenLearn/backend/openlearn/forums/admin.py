from django.contrib import admin
from .models import ForumPost,ForumThread
# Register your models here.
admin.site.register(ForumPost)
admin.site.register(ForumThread)