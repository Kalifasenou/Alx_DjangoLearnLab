# Commande Python :
from bookshelf.models import Book
book = Book.objects.create(title="Sous l'orage", author="Seydou Badian Kouyaté", publication_year=1957)
print(book)

# Output :
<Book: Sous l'orage by Seydou Badian Kouyaté (1957)>
