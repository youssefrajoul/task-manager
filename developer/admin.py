from django.contrib import admin
from .models import Developer
from task.models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import DeveloperForm, DeveloperChangeForm, ShortDeveloperForm


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class DeveloperAdmin(UserAdmin):
    add_form = DeveloperForm
    form = DeveloperChangeForm
    model = get_user_model()
    list_display = ('first_name', 'last_name', 'username', 'is_free')
    inlines = [TaskInline]


admin.site.register(Developer, DeveloperAdmin)
