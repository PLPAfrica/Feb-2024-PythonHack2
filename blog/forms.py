from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from profiles.models import Profile
from .models import BlogPost, Comment
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField


class BlogPostForm(forms.ModelForm):
    content = HTMLField()  # Add parentheses
    author = Profile.user

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'image', 'tags')

    def save(self, commit=True):
        try:
            blog_post = super(BlogPostForm, self).save(commit=False)
            if commit:
                blog_post.save()
                self.save_m2m()
            return blog_post
        except ValidationError as e:  # Catch specific exception
            messages.error("An error occurred while saving the blog post form: {}".format(str(e)))
            raise e


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]
