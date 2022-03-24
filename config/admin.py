from django.contrib import admin
from import_export.admin import ImportExportMixin
from .model import SubscribeEmail
# Register your models here.


class SubscribeEmailAdmin(ImportExportMixin, admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ['email', 'created_at']

admin.site.register(SubscribeEmail,SubscribeEmailAdmin)