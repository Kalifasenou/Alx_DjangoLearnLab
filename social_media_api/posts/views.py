from urllib import response
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Like, Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Create your views here.

#view pour la creation de poste
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#vue pour afficher info d'un poste
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

#vu de creation de commentaire
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        serializer.save(user=self.request.user, post_id=post_id)


#vu de l'option aimer ou non
class LikeToggleView(generics.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
            return response({"message": "Unliked"})
        return response({"message": "Liked"})


#vue de feed
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_ids = user.following.values_list("following_id", flat=True)
        return Post.objects.filter(user_id__in=following_ids).order_by("-created_at")


