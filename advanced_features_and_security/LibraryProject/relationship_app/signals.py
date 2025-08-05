# relationship_app/signals.py
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Ne s’exécute que pour notre app
    if sender.name != 'relationship_app':
        return

    Book = apps.get_model('relationship_app', 'Book')
    ct = ContentType.objects.get_for_model(Book)

    # Définition des groupes et de leurs codenames de permissions
    groups_config = {
        'Editors': ['can_add_book', 'can_change_book'],
        'Viewers': ['view_book'],
        'Admins':  ['can_add_book', 'can_change_book', 'can_delete_book', 'view_book'],
    }

    for group_name, codenames in groups_config.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        for codename in codenames:
            try:
                perm = Permission.objects.get(content_type=ct, codename=codename)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                # Permission non définie : ignore ou log
                pass
