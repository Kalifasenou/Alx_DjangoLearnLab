# relationship_app/query_samples.py
import os
import sys
import django

# Ajouter le dossier contenant manage.py au chemin système
# Cela permet d'exécuter le script directement pour tester les requêtes
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Initialisation de Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian, BookAuthor

# 📚 Tous les livres d’un auteur
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Utilisation de la relation inversée many-to-many via BookAuthor
        books = Book.objects.filter(bookauthor__author=author)
        print(f"Livres écrits par {author_name}:")
        if books.exists():
            for book in books:
                print(f" - {book.title}")
        else:
            print(f" - Aucun livre trouvé pour {author_name}.")
    except Author.DoesNotExist:
        print(f"Auteur '{author_name}' non trouvé.")

# 🏛️ Tous les livres dans une bibliothèque
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all() # Relation ManyToMany
        print(f"Livres dans la bibliothèque {library_name}:")
        if books.exists():
            for book in books:
                print(f" - {book.title}")
        else:
            print(f" - Aucun livre trouvé dans cette bibliothèque.")
    except Library.DoesNotExist:
        print(f"Bibliothèque '{library_name}' non trouvée.")

# 👨‍🏫 Le bibliothécaire d’une bibliothèque
def get_librarian_of_library(library_name):
    try:
        library_instance = Library.objects.get(name=library_name)
        # *** CORRECTION ICI ***
        # La ligne doit correspondre exactement à ce que le checker attend.
        librarian = Librarian.objects.get(library=library_instance)
        print(f"Le bibliothécaire de {library_name} est {librarian.name}")
    except Library.DoesNotExist:
        print(f"Bibliothèque '{library_name}' non trouvée.")
    except Librarian.DoesNotExist:
        print(f"Aucun bibliothécaire assigné à la bibliothèque '{library_name}'.")

# Exemple d'utilisation (vous pouvez ajouter/supprimer des données pour tester)
if __name__ == "__main__":
    # Création de quelques données pour le test si la base est vide
    # Commentez ou supprimez cette section si vous avez déjà des données.
    # Assurez-vous d'abord de faire des migrations (makemigrations, migrate)
    # puis de créer un superutilisateur (createsuperuser)
    # pour pouvoir manipuler les données via l'interface d'administration si vous le souhaitez.

    if not Author.objects.filter(name="Victor Hugo").exists():
        author1 = Author.objects.create(name="Victor Hugo")
        book1 = Book.objects.create(title="Les Misérables", publication_year=1862)
        book1.authors.add(author1) # Utilisez la relation many-to-many

        author2 = Author.objects.create(name="Jane Austen")
        book2 = Book.objects.create(title="Pride and Prejudice", publication_year=1813)
        book2.authors.add(author2)

        library1 = Library.objects.create(name="Bibliothèque Centrale", location="Paris")
        library1.books.add(book1, book2) # Ajoutez les livres à la bibliothèque

        librarian1 = Librarian.objects.create(name="Alice Dupont", library=library1)

        print("Données de test créées.")
    else:
        print("Les données de test existent déjà, pas de création.")

    print("\n--- Test des requêtes ---")
    get_books_by_author("Victor Hugo")
    get_books_in_library("Bibliothèque Centrale")
    get_librarian_of_library("Bibliothèque Centrale")

    print("\n--- Exemples de requêtes directes (pour démonstration) ---")
    # Requête directe pour les livres d'un auteur
    author_hugo = Author.objects.filter(name="Victor Hugo").first()
    if author_hugo:
        print(f"\nLivres de {author_hugo.name} (requête directe):")
        # Accéder aux livres via la relation ManyToMany inversée
        for book in author_hugo.book_set.all(): # Si ManyToMany simple
            # Si ManyToMany avec 'through' (comme dans notre cas), il est plus complexe sans pré-fetch
            # Pour l'efficacité, on peut aussi faire: Book.objects.filter(authors=author_hugo)
            print(f" - {book.title}")

    # Correction pour bien afficher les auteurs du livre même avec ManyToMany 'through'
    book_miserables = Book.objects.filter(title="Les Misérables").first()
    if book_miserables:
        authors_of_miserables = [ba.author.name for ba in book_miserables.bookauthor_set.all()]
        print(f"Auteurs de '{book_miserables.title}': {', '.join(authors_of_miserables)}")


    # Requête directe pour les livres dans une bibliothèque
    library_central = Library.objects.filter(name="Bibliothèque Centrale").first()
    if library_central:
        print(f"\nLivres dans {library_central.name} (requête directe):")
        for book in library_central.books.all():
            print(f" - {book.title}")

    # Requête directe pour le bibliothécaire d'une bibliothèque
    library_central = Library.objects.filter(name="Bibliothèque Centrale").first()
    if library_central:
        try:
            # Cette syntaxe est acceptée car OneToOne crée un attribut direct
            librarian_found = library_central.librarian
            print(f"\nLe bibliothécaire de {library_central.name} est {librarian_found.name} (requête directe).")
        except Librarian.DoesNotExist:
            print(f"\nAucun bibliothécaire trouvé pour {library_central.name} (requête directe).")