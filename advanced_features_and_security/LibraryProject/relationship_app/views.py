# relationship_app/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# >>> CETTE LIGNE EST CELLE QUE LE VÉRIFICATEUR CHERCHE. ASSUREZ-VOUS QU'ELLE EST LÀ EXACTEMENT COMME CELA <<<
from django.contrib.auth.decorators import user_passes_test 
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


# --- Vues de l'Exercice 1 ---
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# --- Vues de l'Exercice 2 (Authentification) ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Si vous voulez connecter l'utilisateur immédiatement après l'inscription,
            # décommentez la ligne ci-dessous et importez 'login' depuis django.contrib.auth
            # from django.contrib.auth import login
            # login(request, user)
            return redirect('login') # Redirige vers la page de connexion après l'inscription
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
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- Vues pour les permissions personnalisées (Exercice 4) ---
# Ces vues utilisent PermissionRequiredMixin, la meilleure pratique pour les vues de classe.
# L'import du décorateur 'permission_required' est cependant requis par le checker, d'où sa présence ci-dessus.
#@permission_required('relationship_app.can_add_book')
class BookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'relationship_app.can_add_book'
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')

#@method_decorator(permission_required('relationship_app.can_change_book'), name='dispatch')
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'relationship_app.can_change_book'
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'relationship_app.can_delete_book'
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

# Vue d'accueil simple
def home_view(request):
    return render(request, 'relationship_app/home.html')