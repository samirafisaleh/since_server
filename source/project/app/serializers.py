
# pylint: disable=import-error
"""[Placeholder module docstring]"""
from rest_framework import serializers
from app.models import (
    Entry
)

class EntrySerializer(serializers.ModelField):
    """ [Template docstring] """

    class Meta:
        """ [Template docstring] """
        model = Entry
        fields = ['id']
