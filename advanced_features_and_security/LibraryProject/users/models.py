from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    # Hérite de UserManager pour conserver create_user/create_superuser standard
    pass

class CustomUser(AbstractUser):
    """
    Hérite d'AbstractUser pour inclure tous les champs par défaut
    (username, first_name, last_name, email, password, etc.)
    et y ajouter date_of_birth et profile_photo.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Remplacer le manager par défaut
    objects = CustomUserManager()

    def __str__(self):
        return self.email or self.username



