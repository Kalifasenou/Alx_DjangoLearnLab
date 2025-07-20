# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books 
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Vue d'accueil (si vous en avez une)
    path('', views.home_view, name='home'), 

    # --- URLs de l'Exercice 1 ---
    path('books/', list_books, name='book-list'), 
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'), 

    # --- URLs de l'Exercice 2 (Authentification) ---
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # --- URLs de l'Exercice 3 (Contrôle d'accès basé sur les rôles) ---
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),

    # --- URLs de l'Exercice 4 (Permissions personnalisées) ---
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]