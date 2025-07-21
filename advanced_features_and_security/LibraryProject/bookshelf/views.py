from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

from advanced_features_and_security.LibraryProject.bookshelf.models import Book


# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
# Logique de création



@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
# Logique d'édition ghttqhth hsryzb tyznzn 
    return "eeeeeeee"


def search_books(request):
    query = request.GET.get('q', '')
    # Méthode sécurisée :
    books = Book.objects.filter(title__icontains=query)