from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportMixin


class ProfileAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Profile,ProfileAdmin)
