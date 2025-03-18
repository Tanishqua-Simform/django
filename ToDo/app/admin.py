from django.contrib import admin
from django.contrib.auth.models import User
from .models import TodoList, ProfilePhoto

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'status', 'assigned_by', 'assigned_to')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'status')
    readonly_fields = ('status','priority')
    actions = ['mark_as_pending', 'mark_as_completed','mark_as_low_priority', 'mark_as_medium_priority', 'mark_as_high_priority']

    def mark_as_pending(self, request, queryset):
        queryset.update(status='pending')
        self.message_user(request, 'Task status updated successfully!')

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, 'Task status updated successfully!')
    
    def mark_as_low_priority(self, request, queryset):
        queryset.update(priority='low')
        self.message_user(request, 'Task priority updated successfully!')
    
    def mark_as_medium_priority(self, request, queryset):
        queryset.update(priority='medium')
        self.message_user(request, 'Task priority updated successfully!')

    def mark_as_high_priority(self, request, queryset):
        queryset.update(priority='high')
        self.message_user(request, 'Task priority updated successfully!')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'user_id')

admin.site.register(TodoList, TodoAdmin)
admin.site.register(ProfilePhoto, ProfileAdmin)
admin.site.site_title = 'ToDo Admin'
admin.site.site_header = 'ToDo Admin Portal'
admin.site.index_title = 'Admin Dashboard'
