from django.db import models

from datetime import datetime

from app.managers import EntryManager

class Entry(models.Model):

    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=250, blank=True)
    datetime_of_interest = models.DateTimeField(blank=False, default=datetime.now)

    objects = models.Manager()
    custom_objects = EntryManager()