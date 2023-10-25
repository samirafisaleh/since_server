
# pylint: disable=import-error
"""[Placeholder module docstring]"""
from datetime import datetime
from django.db import models
from django.utils import timezone
from app.managers import EntryManager

class Entry(models.Model):
    """ [Template docstring] """

    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=250, blank=True)
    datetime_of_interest = models.DateTimeField(blank=False, default=timezone.now)

    created_on = models.DateTimeField(null=False, default=timezone.now)
    deleted_on = models.DateTimeField(null=True)
    modified_on = models.DateTimeField(null=True)

    objects = models.Manager()
    custom_objects = EntryManager()
