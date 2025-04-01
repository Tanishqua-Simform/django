from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CustomBookCreateView, CustomBookUpdateView, CustomBookCreateViewMixin, CustomBookUpdateViewMixin, CustomBookCreateViewGeneric, CustomBookUpdateViewGeneric, custom_create_book, custom_update_book, custom_create_book_decorator, UserList, UserDetail

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('custom/books/', CustomBookCreateView.as_view()),
    path('custom/books/<int:pk>', CustomBookUpdateView.as_view()),
    path('mixin/books/', CustomBookCreateViewMixin.as_view()),
    path('mixin/books/<int:pk>', CustomBookUpdateViewMixin.as_view()),
    path('generic/books/', CustomBookCreateViewGeneric.as_view()),
    path('generic/books/<int:pk>', CustomBookUpdateViewGeneric.as_view()),
    path('function/books/', custom_create_book),
    path('function/books/<int:pk>', custom_update_book),
    path('decorator/books/', custom_create_book_decorator),
    path('decorator/books/<int:pk>', custom_update_book),
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
]
