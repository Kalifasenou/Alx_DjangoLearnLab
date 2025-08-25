# accounts/views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer
)

# 
CustomUser = get_user_model()


# view de creation de compte
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # utiliser CustomUser ici pour être cohérent avec le checkeur
        user = CustomUser.objects.get(username=response.data["username"])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


# view de connexion
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


# view de profils user
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# vues de suivi

# List all users  
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()    
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]


# suivre user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(CustomUser, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"message": f"You are now following {target.username}"}, status=status.HTTP_200_OK)


# ne plus suivre user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(CustomUser, pk=user_id)
        request.user.following.remove(target)
        return Response({"message": f"You unfollowed {target.username}"}, status=status.HTTP_200_OK)


# liste des users suivis
class FollowingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.request.user.following.all()


# liste des users qui nous suivent
class FollowersListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.request.user.followers.all()
