
# pylint: disable=import-error
"""[Placeholder module docstring]"""
from datetime import datetime
from django.db import models
from app.managers import EntryManager

class Entry(models.Model):
    """ [Template docstring] """

    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=250, blank=True)
    datetime_of_interest = models.DateTimeField(blank=False, default=datetime.now)

    objects = models.Manager()
    custom_objects = EntryManager()
