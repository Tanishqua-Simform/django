from django.contrib import admin
from .models import todo_list

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_by')

admin.site.register(todo_list, TodoAdmin)
