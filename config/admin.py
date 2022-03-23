from django.contrib import admin
from import_export.admin import ExportActionMixin
from .model import SubscribeEmail
# Register your models here.


class DataCollectorAdmin(ExportActionMixin, admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ('email', 'created_at')

admin.site.register(SubscribeEmail,DataCollectorAdmin)