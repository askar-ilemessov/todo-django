from django.contrib import admin
from .models import Task


@admin.register(Task)
class AuthorAdmin(admin.ModelAdmin):
    pass
