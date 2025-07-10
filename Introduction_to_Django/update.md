# Commande Python :
from bookshelf.models import Book
# Récupérer le livre à modifier
book_to_update = Book.objects.get(title="Sous l'orage")
# Modifier son titre pour y ajouter la mention "roman"
book_to_update.title = "Sous l'orage (roman)"
# Sauvegarder les modifications dans la base de données
book_to_update.save()
print(book_to_update.title)


# Output:
Sous l'orage (roman)
