from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Article


class ArticleAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['title', 'author']

admin.site.register(Article,ArticleAdmin)