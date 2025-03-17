from django.contrib import admin
from .models import TodoList

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_by')

admin.site.register(TodoList, TodoAdmin)
