from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Author, Book, Library, Librarian, UserProfile


# --- Vues de l'Exercice 1 ---

# Vue basée sur une fonction pour lister tous les livres
def list_books(request):
    books = Book.objects.all()
    # Le chemin du template doit être explicite et correspondre à la structure attendue par le checker
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Vue basée sur une classe pour afficher les détails d'une bibliothèque
# Utilise DetailView comme demandé
class LibraryDetailView(DetailView):
    model = Library # Le modèle associé à cette vue
    # Le chemin du template doit être explicite
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # Nom de la variable passée au template (ex: dans le template on aura {{ library.name }})


# --- Vues de l'Exercice 2 (Authentification) ---
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    # Redirige vers la page d'accueil nommée 'home' après connexion réussie
    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    # Redirige vers la page de connexion nommée 'login' après déconnexion
    next_page = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Le signal (défini dans signals.py et activé dans apps.py) devrait créer automatiquement le UserProfile ici
            return redirect('login') # Redirige vers la page de login après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# --- Fonctions de test de rôle pour l'Exercice 3 ---
# Ces fonctions sont utilisées avec le décorateur @user_passes_test
def is_admin(user):
    # Vérifie si l'utilisateur est authentifié et a le rôle 'Admin'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    # Vérifie si l'utilisateur est authentifié et a le rôle 'Librarian'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    # Vérifie si l'utilisateur est authentifié et a le rôle 'Member'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Vues basées sur les rôles (Exercice 3) ---
@user_passes_test(is_admin, login_url='/login/') # Redirige vers '/login/' si l'utilisateur n'a pas le rôle
def admin_view(request):
    # Le chemin du template doit être explicite
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    # Le chemin du template doit être explicite
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    # Le chemin du template doit être explicite
    return render(request, 'relationship_app/member_view.html')

# --- Vues pour les permissions personnalisées (Exercice 4) ---
# Assurez-vous que votre modèle Book a la classe Meta avec les permissions définies.

class BookCreateView(PermissionRequiredMixin, CreateView):
    # Exige la permission 'can_add_book'
    permission_required = 'relationship_app.can_add_book'
    model = Book
    # Champs à afficher dans le formulaire (ajoutez 'publication_year' si votre modèle l'a)
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html' # Template pour le formulaire de création
    success_url = reverse_lazy('book-list') # Redirige après succès

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    # Exige la permission 'can_change_book'
    permission_required = 'relationship_app.can_change_book'
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html' # Template pour le formulaire de modification
    success_url = reverse_lazy('book-list')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    # Exige la permission 'can_delete_book'
    permission_required = 'relationship_app.can_delete_book'
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html' # Template pour la confirmation de suppression
    success_url = reverse_lazy('book-list') # Redirige après succès

# Vue d'accueil simple (si non fournie ailleurs)
def home_view(request):
    # Un template simple pour la page d'accueil
    return render(request, 'relationship_app/home.html')