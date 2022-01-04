from django.contrib import admin
from .models import Course, Category, SubCategory, DataCollector
# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(DataCollector)

