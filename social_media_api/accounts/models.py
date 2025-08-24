from django.db import models
from django.contrib.auth.models import AbstractUser

# Mes diffs models.
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )
    
    def __str__(self):
        return self.username
    
#follower model
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower} → {self.following}"
