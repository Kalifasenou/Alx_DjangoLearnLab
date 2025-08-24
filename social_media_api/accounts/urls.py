from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserListView, FollowUserView, UnfollowUserView, FollowingListView, FollowersListView



urlpatterns = [
    #inscription 
    path("register/", RegisterView.as_view(), name="register"),   

    #connexion
    path("login/", LoginView.as_view(), name="login"),           

    #profils
    path("profile/", ProfileView.as_view(), name="profile"),     

    # users list (utilisé par le correcteur)
    path("users/", UserListView.as_view(), name="user-list"),

    # follow/unfollow endpoints demandés
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),

    # lists
    path("me/following/", FollowingListView.as_view(), name="my-following"),
    path("me/followers/", FollowersListView.as_view(), name="my-followers"),

]