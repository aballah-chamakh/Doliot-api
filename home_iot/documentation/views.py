from django.shortcuts import render
from rest_framework import generics
from .permissions import IsPublishedOrIsAdmin
from .serializers import SimpleDocumentationSerializer,DocumentationSerializer
from .models import Documentation

class SimpleDocumentationListView(generics.ListAPIView):
    serializer_class = SimpleDocumentationSerializer
    queryset = Documentation.objects.all()
    def get_queryset(self):
        qs = Documentation.objects.filter(published=True)
        return qs

class DocumentationRetrieveView(generics.RetrieveAPIView):
    serializer_class = DocumentationSerializer
    queryset = Documentation.objects.all()
    permissons_classes = (IsPublishedOrIsAdmin,)
    lookup_field = 'slug'
