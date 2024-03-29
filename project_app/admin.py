from django.contrib import admin
from .models import Project, Navbar
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Project)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'desc')


@admin.register(Navbar)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'nav')
