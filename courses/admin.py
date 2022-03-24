from django.contrib import admin
from .models import Course, Category, SubCategory, DataCollector
from import_export.admin import ImportExportMixin
# Register your models here.

class DataCollectorAdmin(ImportExportMixin, admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ('first_name', 'last_name', 'email', 'created_at')

admin.site.register(DataCollector,DataCollectorAdmin)

class CourseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Course,CourseAdmin)

class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Category,CategoryAdmin)

class SubCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['title']

admin.site.register(SubCategory,SubCategoryAdmin)