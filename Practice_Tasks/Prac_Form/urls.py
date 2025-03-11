from django.urls import path
from .views import feedback_form, course_modelform, form_validation, login_form, task_formset, profile_manual

urlpatterns = [
    path('feedback', feedback_form, name="feedback_form"),
    path('course/create', course_modelform, name="course_modelform"),
    path('validate', form_validation, name="form_validation"),
    path('login', login_form, name="login_form"),
    path('task/create', task_formset, name="task_formset"),
    path('profile/create', profile_manual, name="profile_manual"),
]