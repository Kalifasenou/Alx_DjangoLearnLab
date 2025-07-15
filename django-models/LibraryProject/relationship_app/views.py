from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Author, Book, Library, Librarian

from .models import Book

# Create your views here.
def home(request):
    return HttpResponse("Bienvenue dans la bibliothèque !")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


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


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'authors']  
    template_name = 'relationship_app/book_form.html'
    success_url = '/books/' 