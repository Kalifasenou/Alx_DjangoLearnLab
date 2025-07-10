# Commande Python :
from bookshelf.models import Book
# Récupérer le livre à modifier
book_to_update = Book.objects.get(title="1984")
# Modifier son titre pour 
book_to_update.title = "Nineteen Eighty-Four"
# Sauvegarder les modifications dans la base de données
book_to_update.save()
print(book_to_update.title)


# Output:
Nineteen Eighty-Four
