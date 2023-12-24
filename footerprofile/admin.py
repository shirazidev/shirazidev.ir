from django.contrib import admin
from .models import Person
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Person)
class PersonAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'avatar')
