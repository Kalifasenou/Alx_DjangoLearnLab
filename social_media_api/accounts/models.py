from django.db import models
from django.contrib.auth.models import AbstractUser

# Mes diffs models.
class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    # relations de suivis avec nom de l'individu
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
        )
    
    def __str__(self):
        return self.username