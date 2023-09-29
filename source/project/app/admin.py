from django.contrib import admin

from app.models import (
    Entry
)

class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ["title", "datetime_of_interest"]
    exclude = []
    search_fields = ['title']

admin.site.register(Entry, EntryAdmin)