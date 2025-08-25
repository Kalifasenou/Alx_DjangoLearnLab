from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
   

# ViewSets pour posts/comments (si déjà présents, on les conserve)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# les posts des utilisateurs que l'utilisateur courant suit.
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()

        return Post.objects.filter(author__in=following_users).order_by("-created_at")



# Like / Unlike views
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({"detail": "Already liked"}, status=status.HTTP_200_OK)

        # create a notification for the post author (if liker != author)
        if post.author != request.user:
            from notifications.models import Notification
            content_type = ContentType.objects.get_for_model(post)
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target_content_type=content_type,
                target_object_id=post.id
            )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

# ne pas aimer
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
        # Optionally create a notification for unlike (commonly not required)
        return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)