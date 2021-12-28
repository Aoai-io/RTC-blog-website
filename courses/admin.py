from django.contrib import admin
from .models import Course, Category, SubCategory
# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(SubCategory)


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     pass