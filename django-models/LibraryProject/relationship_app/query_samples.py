import os
import django

# Initialisation de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian


# 📚 Tous les livres d’un auteur
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Livres écrits par {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print("Auteur non trouvé.")

# 🏛️ Tous les livres dans une bibliothèque
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Livres dans la bibliothèque {library_name}:")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print("Bibliothèque non trouvée.")

# 👨‍🏫 Le bibliothécaire d’une bibliothèque
def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Le bibliothécaire de {library_name} est {librarian.name}")
    except Library.DoesNotExist:
        print("Bibliothèque non trouvée.")
    except Librarian.DoesNotExist:
        print("Aucun bibliothécaire assigné à cette bibliothèque.")

# Exemple d'utilisation
if __name__ == "__main__":
    get_books_by_author("Victor Hugo")
    get_books_in_library("Bibliothèque Centrale")
    get_librarian_of_library("Bibliothèque Centrale")
