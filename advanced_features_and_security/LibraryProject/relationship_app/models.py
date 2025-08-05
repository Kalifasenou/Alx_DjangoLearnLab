# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings  

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BookAuthor(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    contribution = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('book', 'author')

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField('Author', through='BookAuthor')

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile of {self.user.email}"

# --- Signaux pour UserProfile (Si vous avez un fichier signals.py, placez-les là-bas) ---
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()