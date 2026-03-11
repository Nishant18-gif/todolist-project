from django.contrib import admin
from .models import Task

# Customize admin list view for Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed')  # ye columns dikhenge

# Register Task with customized admin
admin.site.register(Task, TaskAdmin)
