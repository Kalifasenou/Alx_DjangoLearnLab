from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


# Create your tests here.
#test CRUD pour Book avec API REST
class BookAPITest(APITestCase):
    def setUp(self):
        a = Author.objects.create(name="Test Author")
        Book.objects.create(title="Book1", publication_year=2000, author=a)
        Book.objects.create(title="Book2", publication_year=2010, author=a)

    def test_list_books(self):
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        url = reverse('book-list-create')
        a = Author.objects.first()
        data = {'title': 'New Book', 'publication_year': 2021, 'author': a.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_update_delete_book(self):
        book = Book.objects.first()
        detail_url = reverse('book-detail', args=[book.id])

        # GET
        resp = self.client.get(detail_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # PUT
        data = {'title': 'Updated', 'publication_year': 2001, 'author': book.author.id}
        resp = self.client.put(detail_url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated')

        # DELETE
        resp = self.client.delete(detail_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)