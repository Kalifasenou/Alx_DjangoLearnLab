from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentCreateView



urlpatterns = [
    #creer un post
    path("posts/", PostListCreateView.as_view(), name="posts"),

    #voir un post
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    #voir commentaire d'un post
    path("posts/<int:post_id>/comments/", CommentCreateView.as_view(), name="add-comment"),
]
