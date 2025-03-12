from django.urls import path
from .views import feedback_form, course_modelform, form_validation, login_form, task_formset, profile_manual, contact_form, booking_form, feedback_form_validate, profile_form_redirect, dashboard

urlpatterns = [
    path('feedback', feedback_form, name="feedback_form"),
    path('course/create', course_modelform, name="course_modelform"),
    path('validate', form_validation, name="form_validation"),
    path('login', login_form, name="login_form"),
    path('task/create', task_formset, name="task_formset"),
    path('profile/create', profile_manual, name="profile_manual"),
    path('contact', contact_form, name="contact_form"),
    path('booking', booking_form, name="booking_form"),
    path('feedback/validate', feedback_form_validate, name="feedback_form_validate"),
    path('dashboard', dashboard, name="dashboard"),
    path('profile/redirect', profile_form_redirect, name="profile_form_redirect"),
]