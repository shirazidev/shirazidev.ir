from django.contrib import admin
from .models import Work
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Work)
class WorkAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title', 'tarikh', 'desc')
