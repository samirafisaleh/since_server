from django.contrib import admin

from app.models import (
    Entry
)

class EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)