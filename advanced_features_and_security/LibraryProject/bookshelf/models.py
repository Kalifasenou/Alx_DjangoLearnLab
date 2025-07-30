from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Manager personnalisé pour CustomUser.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True and is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()
    
    def __str__(self):
         return self.email or self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField() 

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        permissions = [
            ("can_view", "Peut voir les livres"),
            ("can_create", "Peut créer des livres"),
            ("can_edit", "Peut modifier des livres"),
            ("can_delete", "Peut supprimer des livres"),
        ]


