from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)  
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs.get("username"),
            password=attrs.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        token, _ = Token.objects.get_or_create(user=user)  # 🔑 renvoie le token
        attrs["user"] = user
        attrs["token"] = token.key
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "bio", "profile_picture", "followers"]
