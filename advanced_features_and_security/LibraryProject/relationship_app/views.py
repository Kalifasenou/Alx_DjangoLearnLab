from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Book, Library, Librarian


# --- Liste des livres (permission view) ---
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# --- Détail d’une bibliothèque ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- CRUD Livre avec permissions personnalisées ---
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'publication_year', 'authors']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'bookshelf.can_create'

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'authors']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'bookshelf.can_edit'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'bookshelf.can_delete'

# --- Dashboards par rôle ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- Inscription et authentification ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# --- Vue d’accueil simple ---
def home_view(request):
    return render(request, 'relationship_app/home.html')
