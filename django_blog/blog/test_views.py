from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
    def test_create_requires_login(self):
        url = reverse('post-create')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)  # redirect to login
        self.client.login(username='u', password='p')
        resp = self.client.post(url, {'title': 't', 'content': 'c'})
        self.assertEqual(Post.objects.count(), 1)
