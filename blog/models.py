from django.db import models
from django.contrib.auth.models import User  # Import the User model
from django.utils import timezone
from profiles.models import Profile
from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    preview = HTMLField(blank=True)
    content = HTMLField(blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    publication_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    author = models.ForeignKey(Profile, default=1, on_delete=models.CASCADE)  # Add the author field

    def profile_picture(self):
        return self.author.profile_picture

    def full_name(self):
        return self.author.user_id

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    # author_name = models.CharField(max_length=100, null=True, blank=True)
    comment_text = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, default=1, on_delete=models.CASCADE)  # Add the author field
    #replies = models.ForeignKey(CommentReply, on_delete=models.CASCADE, related_name='replies')

    def profile_picture(self):
        return self.author.profile_picture

    def full_name(self):
        return self.author.user_id

    def __str__(self):
        return f'Comment by {self.author.user.get_full_name()} on {self.blog_post}'


class CommentReply(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    # author_name = models.CharField(max_length=100, null=True, blank=True)
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, default=1, on_delete=models.CASCADE)  # Add the author field

    def profile_picture(self):
        return self.author.profile_picture

    def full_name(self):
        return self.author.user_id

    def __str__(self):
        return (f'Replied to {self.comment} from {self.comment.author.user.get_full_name()} by '
                f'{self.author.user.get_full_name()} on {self.blog_post}')
