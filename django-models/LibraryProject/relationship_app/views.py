from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .models import Author, Book, Library, Librarian

from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.forms import UserCreationForm 

from django.contrib.auth.decorators import user_passes_test 
from django.shortcuts import redirect

from django.contrib.auth.mixins import PermissionRequiredMixin 





from .models import Book

# Create your views here.
def home(request):
    return HttpResponse("Bienvenue dans la bibliothèque !")

def book_list(request):
    books = Book.objects.all() # 
    return render(request, 'relationship_app/book_list.html', {'books': books}) # 


# Listes
class AuthorListView(ListView):
    model = Author
    template_name = 'relationship_app/author_list.html'

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/book_list.html'

class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'

# Détails
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'relationship_app/author_detail.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


# Vues avec permissions (Correction et ajouts)
class BookCreateView(PermissionRequiredMixin, CreateView): # Ajoutez PermissionRequiredMixin
    permission_required = 'relationship_app.can_add_book' # Spécifiez la permission requise
    model = Book
    fields = ['title', 'publication_year', 'authors']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(PermissionRequiredMixin, UpdateView): # Nouvelle vue
    permission_required = 'relationship_app.can_change_book'
    model = Book
    fields = ['title', 'publication_year', 'authors']
    template_name = 'relationship_app/book_form.html' # Réutiliser le formulaire
    success_url = reverse_lazy('book-list')

class BookDeleteView(PermissionRequiredMixin, DeleteView): # Nouvelle vue
    permission_required = 'relationship_app.can_delete_book'
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html' # Créez ce template
    success_url = reverse_lazy('book-list')



class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    # next_page est géré par LOGIN_REDIRECT_URL dans settings.py par défaut

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    # next_page est géré par LOGOUT_REDIRECT_URL dans settings.py par défaut

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login') # Redirige vers la page de connexion après inscript



# Fonctions de test de rôle
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Vues basées sur les rôles
@user_passes_test(is_admin, login_url='/login/') # Redirige vers la page de login si non admin
def admin_view(request):
    return HttpResponse("Bienvenue, Admin ! Contenu réservé aux administrateurs.")

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return HttpResponse("Bienvenue, Bibliothécaire ! Contenu réservé aux bibliothécaires.")

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return HttpResponse("Bienvenue, Membre ! Contenu réservé aux membres.")

# Fonctions de test de rôle
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Vues basées sur les rôles
@user_passes_test(is_admin, login_url='/login/') # Redirige vers la page de login si non admin
def admin_view(request):
    return HttpResponse("Bienvenue, Admin ! Contenu réservé aux administrateurs.")

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return HttpResponse("Bienvenue, Bibliothécaire ! Contenu réservé aux bibliothécaires.")

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return HttpResponse("Bienvenue, Membre ! Contenu réservé aux membres.")


