from django import forms
from django.contrib import messages
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        content = forms.CharField(widget=forms.HiddenInput())
        fields = ('title', 'content', 'image', 'tags')

    def save(self, commit=True):
        try:
            blog_post = super(BlogPostForm, self).save(commit=False)
            if commit:
                blog_post.save()
                self.save_m2m()
            return blog_post
        except Exception as e:
            messages.error("An error occurred while saving the blog post form: {}".format(str(e)))
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
            messages.error("An error occurred while saving the comment form: {}".format(str(e)))
            raise e
