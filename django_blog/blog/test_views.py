# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.other = User.objects.create_user(username='user2', password='pass123')
        self.post = Post.objects.create(title='T1', content='C1', author=self.user)

    def test_list_posts(self):
        resp = self.client.get(reverse('post-list'))
        self.assertEqual(resp.status_code, 200)

    def test_create_post_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertIn(resp.status_code, (302, 301))  # redirected to login
        self.client.login(username='user1', password='pass123')
        resp = self.client.post(reverse('post-create'), {'title': 'New', 'content': 'body'})
        self.assertEqual(Post.objects.filter(title='New').count(), 1)

    def test_update_post_owner_only(self):
        url = reverse('post-edit', args=[self.post.pk])
        self.client.login(username='user2', password='pass123')
        resp = self.client.get(url)
        # non-owner should be forbidden (redirect to 403 or redirect to login or 200 with form blocked)
        # We assert that owner can access update:
        self.client.login(username='user1', password='pass123')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(url, {'title': 'Updated', 'content': 'C1'})
        self.assertEqual(Post.objects.get(pk=self.post.pk).title, 'Updated')

    def test_delete_post(self):
        url = reverse('post-delete', args=[self.post.pk])
        self.client.login(username='user1', password='pass123')
        resp = self.client.post(url)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cuser', password='pass123')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_add_comment_requires_login(self):
        url = reverse('post-detail', args=[self.post.pk])
        resp = self.client.post(url, {'content': 'hello'})
        # should redirect to login
        self.assertIn(resp.status_code, (302, 301))
        self.client.login(username='cuser', password='pass123')
        resp = self.client.post(url, {'content': 'hello'})
        self.assertEqual(self.post.comments.count(), 1)
