# Commande Python :
from bookshelf.models import Book
# Récupérer le livre par son titre
retrieved_book = Book.objects.get(title="1984")
print(f"Titre: {retrieved_book.title}")
print(f"Auteur: {retrieved_book.author}")
print(f"Année de publication: {retrieved_book.publication_year}")

# Output :
Titre: 1984
Auteur: George Orwell
Année de publication: 1949
