from django.test import TestCase
from django.urls import reverse
from .jsonplaceholder import fetch_posts, fetch_post_details

class PostViewTests(TestCase):
    
    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        # Assuming post_id 1 exists
        response = self.client.get(reverse('post_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_posts(self):
        posts = fetch_posts()
        self.assertTrue(len(posts) > 0)

    def test_fetch_post_details(self):
        post = fetch_post_details(1)
        self.assertIsNotNone(post)
        self.assertTrue(len(post.comments) > 0)