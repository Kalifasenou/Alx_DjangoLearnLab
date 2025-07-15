from django.db import models

# Modèle Auteur
class Author(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

# Modèle intermédiaire entre Book et Author
class BookAuthor(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    contribution = models.CharField(max_length=100, blank=True, null=True)  # Optionnel

    class Meta:
        unique_together = ('book', 'author')  # pour éviter les doublons

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"

# Modèle Livre
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField('Author', through='BookAuthor')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    #books_by_author = Book.objects.filter(authors=author)


    def __str__(self):
        return self.title

# Modèle Bibliothèque
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)


    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
