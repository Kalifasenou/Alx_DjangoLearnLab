# Commande Python :
from bookshelf.models import Book
# Récupérer le livre par son titre
retrieved_book = Book.objects.get(title="Sous l'orage")
print(f"Titre: {retrieved_book.title}")
print(f"Auteur: {retrieved_book.author}")
print(f"Année de publication: {retrieved_book.publication_year}")

# Output :
Titre: Sous l'orage
Auteur: Seydou Badian Kouyaté
Année de publication: 1957
