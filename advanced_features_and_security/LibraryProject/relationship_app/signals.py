from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Book, UserProfile
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()




# Création des groupes
editors, _ = Group.objects.get_or_create(name='Editors')
viewers, _ = Group.objects.get_or_create(name='Viewers')
admins,  _ = Group.objects.get_or_create(name='Admins')

# Récupération de permissions (exemple sur le modèle Book)
content_type = ContentType.objects.get_for_model(Book)
perm_add = Permission.objects.get(content_type=content_type, codename='can_add_book')
perm_edit = Permission.objects.get(content_type=content_type, codename='can_change_book')
perm_delete = Permission.objects.get(content_type=content_type, codename='can_delete_book')
perm_view = Permission.objects.get(content_type=content_type, codename='view_book')

# Assignation des permissions aux groupes
editors.permissions.add(perm_add, perm_edit)
viewers.permissions.add(perm_view)
admins.permissions.set([perm_add, perm_edit, perm_delete, perm_view])  # tous droits
