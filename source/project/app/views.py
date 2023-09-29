
# pylint: disable=import-error
"""[Placeholder module docstring]"""
from django.shortcuts import render
from rest_framework import viewsets
from app.models import (
    Entry
)
from app.serializers import (
    EntrySerializer
)

class EntryViewSet(viewsets.ModelViewSet):
    """ [Template docstring] """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def create(self, request, *args, **kwargs):
        """ [Template function docstring] """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ [Template function docstring] """
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """ [Template function docstring] """
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """ [Template function docstring] """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """ [Template function docstring] """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """ [Template function docstring] """
        return super().destroy(request, *args, **kwargs)
