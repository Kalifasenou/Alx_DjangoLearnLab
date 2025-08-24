from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentCreateView, LikeToggleView, FeedView



urlpatterns = [
    #creer un post
    path("posts/", PostListCreateView.as_view(), name="posts"),

    #voir un post
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    #voir commentaire d'un post
    path("posts/<int:post_id>/comments/", CommentCreateView.as_view(), name="add-comment"),
]


#route d'aimer ou pas
urlpatterns += [
    path("posts/<int:post_id>/like/", LikeToggleView.as_view(), name="like-toggle"),
]


#route pour le feed
urlpatterns += [
    path("feed/", FeedView.as_view(), name="feed"),
]

