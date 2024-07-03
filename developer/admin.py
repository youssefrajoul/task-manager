from django.contrib import admin
from .models import Developer
from task.models import Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_free')
    inlines = [TaskInline]


admin.site.register(Developer, DeveloperAdmin)
