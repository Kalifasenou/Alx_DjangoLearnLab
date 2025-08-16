# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # posts CRUD
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # comments
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # tags & search
    path('tags/<slug:tag>/', views.TaggedPostListView.as_view(), name='posts-by-tag'),
    path('search/', views.PostSearchView.as_view(), name='post-search'),
]
