from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass1234")
        self.author = Author.objects.create(name="Test Author")
        Book.objects.create(title="Book1", publication_year=2000, author=self.author)
        Book.objects.create(title="Book2", publication_year=2010, author=self.author)

    def test_list_books(self):
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_requires_authentication(self):
        url = reverse('book-list-create')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}

        # Sans authentification → devrait échouer
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # Avec authentification
        self.client.login(username="tester", password="pass1234")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_and_delete_book_requires_authentication(self):
        book = Book.objects.first()
        detail_url = reverse('book-detail', args=[book.id])
        data = {'title': 'Updated', 'publication_year': 2001, 'author': book.author.id}

        # Sans authentification → devrait échouer
        resp = self.client.put(detail_url, data, format='json')
        self.assertIn(resp.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # Authentifié
        self.client.login(username="tester", password="pass1234")
        resp = self.client.put(detail_url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated')

        resp = self.client.delete(detail_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
