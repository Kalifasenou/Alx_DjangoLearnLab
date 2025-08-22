from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import FollowUserView


# routes d'acces aux diff views
urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("profile", ProfileView.as_view(), name="profile"),
    ]



#route d'acces de suivi
urlpatterns += [
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-unfollow"),
]
