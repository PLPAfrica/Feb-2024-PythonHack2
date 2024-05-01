from django.test import TestCase
from django.utils import timezone
from .models import BlogPost, Tag
from profiles.models import Profile

class BlogPostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a dummy user profile for the author
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        profile = Profile.objects.create(user=user, profile_picture='profile.jpg')

        # Create a dummy tag
        tag = Tag.objects.create(name='Test Tag')

        # Create a dummy blog post
        BlogPost.objects.create(
            title='Test Title',
            content='<p>This is a test blog post content.</p>',
            publication_date=timezone.now(),
            author=profile,
        )

    def test_title_content(self):
        blog_post = BlogPost.objects.get(id=1)
        expected_title = f'{blog_post.title}'
        self.assertEquals(expected_title, 'Test Title')

    def test_content_content(self):
        blog_post = BlogPost.objects.get(id=1)
        expected_content = f'{blog_post.content}'
        self.assertEquals(expected_content, '<p>This is a test blog post content.</p>')

    def test_author_content(self):
        blog_post = BlogPost.objects.get(id=1)
        expected_author = f'{blog_post.author}'
        self.assertEquals(expected_author, 'testuser')

    def test_str_representation(self):
        blog_post = BlogPost.objects.get(id=1)
        expected_str = f'{blog_post.title}'
        self.assertEquals(expected_str, str(blog_post))
