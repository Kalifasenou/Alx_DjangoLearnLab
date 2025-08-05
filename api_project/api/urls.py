# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ta liste simple
    path('books/', BookList.as_view(), name='book-list'),
    # toutes les routes CRUD
    path('', include(router.urls)),
]
