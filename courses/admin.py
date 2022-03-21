from django.contrib import admin
from .models import Course, Category, SubCategory, DataCollector
# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(SubCategory)

class DataCollectorAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(DataCollector,DataCollectorAdmin)