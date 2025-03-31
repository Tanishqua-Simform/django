from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CustomBookCreateView

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('custom/books/', CustomBookCreateView.as_view()),
]
