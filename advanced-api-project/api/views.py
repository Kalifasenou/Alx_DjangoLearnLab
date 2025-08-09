# api/views.py

from rest_framework import generics, viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# api/views.py (en-tête recommandé)
from rest_framework import generics, viewsets, filters
from rest_framework.permissions import AllowAny
import django_filters.rest_framework

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer



# 1️⃣ Liste tous les livres (GET /books/)
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # lecture ouverte


# 2️⃣ Récupère un livre par PK (GET /books/<pk>/)
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# 3️⃣ Crée un livre (POST /books/create/)
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # seuls les utilisateurs authentifiés peuvent créer


# 4️⃣ Met à jour un livre (PUT/PATCH /books/<pk>/update/)
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# 5️⃣ Supprime un livre (DELETE /books/<pk>/delete/)
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# 6️⃣ List/Create avec filtres, recherche et ordonnancement (GET/POST /books/)
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


# 7️⃣ Retrieve/Update/Destroy (GET/PUT/DELETE /books/<pk>/)
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 8️⃣ ViewSet complet pour Author (CRUD via router)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
