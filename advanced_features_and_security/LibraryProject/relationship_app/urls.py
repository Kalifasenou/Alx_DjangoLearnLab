from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views
from .views import (
    LibraryDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # Accueil
    path('', views.home_view, name='home'),

    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html',
                                                 next_page=reverse_lazy('login')), name='logout'),
    path('register/', views.register, name='register'),

    # Gestion des livres
    path('books/', views.book_list, name='book-list'),
    path('books/new/', BookCreateView.as_view(), name='book-add'),
    path('books/edit/<int:pk>/', BookUpdateView.as_view(), name='book-edit'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),

    # Détail d’une bibliothèque
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Dashboards par rôle
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),
]
