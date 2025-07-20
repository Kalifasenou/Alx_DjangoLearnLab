# relationship_app/urls.py
from django.urls import path
from . import views
# *** CORRECTION ICI *** : Importez les vues d'authentification directement de Django
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy # Assurez-vous d'importer reverse_lazy ici aussi si vous l'utilisez pour next_page

urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.list_books, name='book-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # --- URLs de l'Exercice 2 (Authentification) ---
    # *** CORRECTION ICI *** : Utilisation directe des vues d'authentification de Django
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # Pour LogoutView, next_page peut être défini directement ou via settings.LOGOUT_REDIRECT_URL
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('register/', views.register, name='register'), # La vue register reste une fonction personnalisée

    # --- URLs de l'Exercice 3 (Contrôle d'accès basé sur les rôles) ---
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),

    # --- URLs de l'Exercice 4 (Permissions personnalisées) ---
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]