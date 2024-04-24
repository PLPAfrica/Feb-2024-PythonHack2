from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost, Comment
import logging

logger = logging.getLogger(__name__)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'tags')

    def save(self, commit=True):
        try:
            blog_post = super(BlogPostForm, self).save(commit=False)
            if commit:
                blog_post.save()
                self.save_m2m()
            return blog_post
        except Exception as e:
            logger.error("Error saving blog post form: %s\n%s", e, e.__traceback__)
            raise e


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'comment_text')

    def save(self, commit=True):
        try:
            comment = super(CommentForm, self).save(commit=False)
            if commit:
                comment.save()
            return comment
        except Exception as e:
            logger.error("Error saving comment form: %s\n%s", e, e.__traceback__)
            raise e
