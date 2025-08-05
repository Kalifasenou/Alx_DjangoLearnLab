# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.list_books, name='book-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # --- URLs de l'Exercice 2 (Authentification) ---
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', next_page=reverse_lazy('login')), name='logout'),
    path('register/', views.register, name='register'),

    # --- URLs de l'Exercice 3 (Contrôle d'accès basé sur les rôles) ---
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),

    # --- URLs de l'Exercice 4 (Permissions personnalisées) ---
    path('add_book/', views.BookCreateView.as_view(), name='book-add'),
    path('edit_book/<int:pk>/', views.BookUpdateView.as_view(), name='book-edit'),
    path('delete_book/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
    
]