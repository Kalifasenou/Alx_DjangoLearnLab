# Commande Python :
from bookshelf.models import Book
# Récupérer le livre à modifier
book = Book.objects.get(title="1984")
# Modifier son titre pour 
book.title = "Nineteen Eighty-Four"
# Sauvegarder les modifications dans la base de données
book.save()
print(book.title)


# Output:
Nineteen Eighty-Four
