from django.contrib import admin

from app.models import (
    Entry
)

class EntryAdmin(admin.ModelAdmin):

    @admin.action(description="Does something")
    def does_something(modeladmin, request, queryset):
        pass


    readonly_fields = ["title", "datetime_of_interest", "description"]
    exclude = []
    search_fields = ['title']
    list_display = ['title', 'datetime_of_interest']
    empty_value_display = "-empty-"
    actions = [does_something]


admin.site.register(Entry, EntryAdmin)