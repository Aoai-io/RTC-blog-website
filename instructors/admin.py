from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Instructor
# Register your models here.


class InstructorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'user', 'specialization']

admin.site.register(Instructor,InstructorAdmin)