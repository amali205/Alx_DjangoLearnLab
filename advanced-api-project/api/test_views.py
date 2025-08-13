from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.book = Book.objects.create(title='Django 101', author='John Doe', publication_year=2020)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='pass1234')
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': 'Jane Doe', 'publication_year': 2021}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': 'Jane Doe', 'publication_year': 2021}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testuser', password='pass1234')
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Django', 'author': 'John Doe', 'publication_year': 2022}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Django')

    def test_delete_book(self):
        self.client.login(username='testuser', password='pass1234')
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('book-list') + '?author=John Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == 'John Doe' for book in response.data))

    def test_search_books(self):
        url = reverse('book-list') + '?search=Django'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Django' in book['title'] for book in response.data))

    def test_order_books(self):
        Book.objects.create(title='A Book', author='Someone', publication_year=2019)
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
