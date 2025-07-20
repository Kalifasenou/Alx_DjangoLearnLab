from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required # Assurez-vous d'avoir permission_required ici
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Author, Book, Library, Librarian, UserProfile # Assurez-vous d'importer tous les modèles nécessaires

# --- Vues de l'Exercice 1 ---

# Vue basée sur une fonction pour lister tous les livres
def list_books(request):
    books = Book.objects.all()
    # *** CORRECTION ICI *** : Spécifiez le chemin complet du template
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Vue basée sur une classe pour afficher les détails d'une bibliothèque
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html' # Spécifiez le chemin complet du template
    context_object_name = 'library' # Nom de la variable passée au template

# --- Vues de l'Exercice 2 (Authentification) ---
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    def get_success_url(self):
        return reverse_lazy('home') # Redirige vers la page d'accueil après connexion

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login') # Redirige vers la page de connexion après déconnexion

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Le signal create_user_profile devrait créer automatiquement le UserProfile ici
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# --- Fonctions de test de rôle pour l'Exercice 3 ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Vues basées sur les rôles (Exercice 3) ---
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    # *** CORRECTION ICI *** : Spécifiez le chemin complet du template
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    # *** CORRECTION ICI *** : Spécifiez le chemin complet du template
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    # *** CORRECTION ICI *** : Spécifiez le chemin complet du template
    return render(request, 'relationship_app/member_view.html')

# --- Vues pour les permissions personnalisées (Exercice 4) ---
# Assurez-vous que vos modèles (Book) ont la classe Meta avec les permissions définies.

class BookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'relationship_app.can_add_book'
    model = Book
    fields = ['title', 'publication_year', 'authors'] # Assurez-vous que 'authors' est gérable via ModelForm si ManyToMany
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'relationship_app.can_change_book'
    model = Book
    fields = ['title', 'publication_year', 'authors']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'relationship_app.can_delete_book'
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

# Vue d'accueil simple (si vous en avez une)
def home_view(request):
    return render(request, 'relationship_app/home.html')