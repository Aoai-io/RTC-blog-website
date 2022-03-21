from django.contrib import admin
from .models import Course, Category, SubCategory, DataCollector
from import_export.admin import ExportActionMixin
# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(SubCategory)

class DataCollectorAdmin(ExportActionMixin, admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ('first_name', 'last_name', 'email', 'created_at')

admin.site.register(DataCollector,DataCollectorAdmin)