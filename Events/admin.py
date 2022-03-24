from django.contrib import admin
from .models import Event
from import_export.admin import ImportExportMixin

# Register your models here.

class EventAdmin(ImportExportMixin, admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ('title', 'date', 'city', 'created_at')

admin.site.register(Event,EventAdmin)
