from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import Follow, User
from rest_framework import status




# Mes views.

#view de creation de compte
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data["username"]) # creation de compte
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


#view de connexion
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


#view de profils user
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    


#vue de suivi
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = User.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"})

    def delete(self, request, user_id):
        user_to_unfollow = User.objects.get(id=user_id)
        Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"})
