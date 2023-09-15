
from rest_framework import serializers
from app.models import (
    Entry
)

class EntrySerializer(serializers.ModelField):

    class Meta:
        model = Entry
        fields = ['id']