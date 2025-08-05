from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    BookListCreate, BookRetrieveUpdateDestroy, AuthorViewSet
)

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('books/',                ListView.as_view(),                name='book-list'),
    path('books/<int:pk>/',       DetailView.as_view(),              name='book-detail'),
    path('books/create/',         CreateView.as_view(),              name='book-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(),             name='book-update'),
    path('books/delete/<int:pk>/', DeleteView.as_view(),             name='book-delete'),

    # Endpoints combinés List+Create / Retrieve+Update+Destroy
    path('books-all/',            BookListCreate.as_view(),          name='book-list-create'),
    path('books-all/<int:pk>/',   BookRetrieveUpdateDestroy.as_view(), name='book-detail-rud'),

    path('', include(router.urls)),
]
