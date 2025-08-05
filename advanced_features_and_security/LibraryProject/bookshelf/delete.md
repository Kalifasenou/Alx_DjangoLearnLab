# Commande Python :
from bookshelf.models import Book
# Récupérer le livre à supprimer par son titre mis à jour
book = Book.objects.get(title="Nineteen Eighty-Four")
# Supprimer l'instance du livre de la base de données
book.delete()

# Vérifier que le livre n'existe plus en tentant de récupérer tous les livres
print(Book.objects.all())


# Output :
<QuerySet []>
