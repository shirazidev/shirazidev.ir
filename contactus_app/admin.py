from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ('subject', 'name', 'email', 'وضعیت_پاسخگویی')
