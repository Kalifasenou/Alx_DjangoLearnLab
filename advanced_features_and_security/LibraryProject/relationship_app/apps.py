from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    name = 'relationship_app'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import relationship_app.signals   # le signal est branché
