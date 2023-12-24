from django.contrib import admin
from .models import Project

@admin.register(Project)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')

