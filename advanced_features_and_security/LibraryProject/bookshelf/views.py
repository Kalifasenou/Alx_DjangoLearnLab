from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logique de création



@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Logique d'édition 

