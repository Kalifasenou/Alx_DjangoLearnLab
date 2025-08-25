from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType




class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.CharField(source="actor.username", read_only=True)
    recipient = serializers.CharField(source="recipient.username", read_only=True)
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["id", "actor", "verb", "target_repr", "unread", "timestamp", "recipient"]

    def get_target_repr(self, obj):
        if obj.target is None:
            return None
        # represent the target simply
        return str(obj.target)
