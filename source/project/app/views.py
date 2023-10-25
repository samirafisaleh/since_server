
# pylint: disable=import-error
"""[Placeholder module docstring]"""
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime
from django.core import exceptions
from app.models import (
    Entry
)
from rest_framework import serializers
from rest_framework.parsers import JSONParser
import io

class CreateSerializer(serializers.ModelSerializer):
    """ [Template docstring] """

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        """ [Template docstring] """
        model = Entry
        fields = ['id',
                  'title',
                  'description',
                  'datetime_of_interest'
                  ]


class EntrySerializer(serializers.ModelSerializer):
    """ [Template docstring] """

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        """ [Template docstring] """
        model = Entry
        fields = ['id',
                  'title',
                  'description',
                  'datetime_of_interest'
                  ]


class EntryViewSet(viewsets.ModelViewSet):
    """ [Template docstring] """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    ##########################
    #
    #
    ##########################
    def create(self, request):
        """ [Template function docstring] """

        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid() == False:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer.save()
        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)

    ##########################
    #
    #
    ##########################
    def retrieve(self, request, pk=None):

        try:
            obj = Entry.objects.get(id=pk)
        except exceptions.ObjectDoesNotExist as e:
            return Response({"message" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError as e:
            return Response({"message" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.get_serializer(obj)
        return Response({"data" : serializer.data}, status=status.HTTP_200_OK)

    ##########################
    #
    #
    ##########################
    def list(self, request):
        """ [Template function docstring] """
        try:
            obj = Entry.objects.filter().order_by('datetime_of_interest')

        except exceptions.ObjectDoesNotExist as e:
            return Response({"message" : str(e)}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    ##########################
    #
    #
    ##########################
    def update(self, request, pk=None):
        """ [Template function docstring] """
        return Response({"data" : []}, status=status.HTTP_200_OK)

    ##########################
    #
    #
    ##########################
    def partial_update(self, request, pk=None):
        """ [Template function docstring] """
        return Response({"data" : []}, status=status.HTTP_200_OK)

    ##########################
    #
    #
    ##########################
    def destroy(self, request, pk=None):
        """ [Template function docstring] """
        try:
            Entry.objects.get(id=pk).delete()
        except exceptions.ObjectDoesNotExist as e:
            pass

        return Response({"message" : True}, status=status.HTTP_200_OK)
