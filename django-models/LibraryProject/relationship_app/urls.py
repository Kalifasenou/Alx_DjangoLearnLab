from django.urls import path
from . import views
#from relationship_app.views import BookCreateView 

urlpatterns = [
    path('', views.home, name='home'),
    #path('books/', views.book_list, name='book-list'),

    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    path('libraries/', views.LibraryListView.as_view(), name='library-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    path('books/add/', views.BookCreateView.as_view(), name='book-add'),

    # Authentification
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),


    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),


    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),


    path('books/add/', views.BookCreateView.as_view(), name='book-add'), # Déjà là, mais avec permission
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'), # Nouvelle URL
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'), # Nouvelle URL


]
