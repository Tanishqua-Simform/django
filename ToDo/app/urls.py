from django.urls import path
from app.views import my_todos, register_user, login_user, logout_user, pending_todos, completed_todos, details, create_todo, create_todo_model, update_todo, delete_todo, upload_profile, show_profile, assigned
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', my_todos, name='my_todos'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', show_profile, name='show_profile'),
    path('upload_profile/', upload_profile, name='upload_profile'),
    path('pending/', pending_todos, name='pending_todos'),
    path('completed/', completed_todos, name='completed_todos'),
    path('assigned/', assigned, name='assigned'),
    path('create/', create_todo_model, name='create_todo'),
    path('create_todo/', create_todo, name='create_todo_form'),
    path('details/<int:task_id>', details, name='details'),
    path('update/<int:task_id>', update_todo, name='update'),
    path('delete/<int:task_id>', delete_todo, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)