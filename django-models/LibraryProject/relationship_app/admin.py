from django.contrib import admin
from .models import Author, Book, Library, Librarian, BookAuthor

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Library)
admin.site.register(Librarian)
