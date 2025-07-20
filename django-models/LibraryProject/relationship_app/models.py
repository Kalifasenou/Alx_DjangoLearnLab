from django.db import models
from django.contrib.auth.models import User

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
    authors = models.ManyToManyField(Author, through='BookAuthor')

    class Meta:
        #  permissions
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

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


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

