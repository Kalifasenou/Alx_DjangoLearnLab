from django.urls import path
from .views import RegisterView, LoginView, ProfileView

# routes d'acces aux diff views
urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("profile", ProfileView.as_view(), name="profile"),
    ]