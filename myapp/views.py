from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blogpost = self.get_object()
        # add logic here to like post
        return Response({'status': 'blog post like'})
