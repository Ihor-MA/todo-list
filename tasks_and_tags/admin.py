from django.contrib import admin

from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "task_created", "deadline", "is_task_done"]


admin.site.register(Tag)
