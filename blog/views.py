from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

import weather
from .forms import BlogPostForm
from django.contrib import messages
from .models import BlogPost
from django.contrib.auth.decorators import login_required
import logging
# from weather.utils import get_weather_data_for_location  # Import the utility function from the weather app
from django.contrib.auth.forms import UserCreationForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


def post_list(request):
    try:
        posts = BlogPost.objects.all().order_by('-publication_date')
        return render(request, 'post_list.html', {'posts': posts})
    except Exception as e:
        logger.error("Error fetching post list: %s\n%s", e, e.__traceback__)
        messages.error(request, 'An error occurred while fetching the post list. Please try again.')
        return redirect('post_list')


def post_detail(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        return render(request, 'post_detail.html', {'post': post})
    except Exception as e:
        logger.error("Error fetching post detail: %s\n%s", e, e.__traceback__)
        messages.error(request, 'An error occurred while fetching the post details. Please try again.')
        return redirect('post_list')


@login_required
def post_create(request):
    try:
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, f'Post "{post.title}" has been successfully created!')
                return redirect('post_detail', pk=post.pk)
        else:
            form = BlogPostForm()
        return render(request, 'post_edit.html', {'form': form})
    except Exception as e:
        logger.error("Error creating a new post: %s\n%s", e, e.__traceback__)
        messages.error(request, 'An error occurred while creating a new post. Please try again.')
        return redirect('post_create')


@login_required
def post_edit(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        if request.method == 'POST':
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, f'Post "{post.title}" has been successfully updated!')
                return redirect('post_detail', pk=post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})
    except Exception as e:
        logger.error("Error editing post: %s\n%s", e, e.__traceback__)
        messages.error(request, 'An error occurred while editing the post. Please try again.')
        return redirect('post_edit', pk=pk)


@login_required
def post_delete(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        post.delete()
        messages.success(request, 'Post has been successfully deleted!')
        return redirect('post_list')
    except Exception as e:
        logger.error("Error deleting post: %s\n%s", e, e.__traceback__)
        messages.error(request, 'An error occurred while deleting the post. Please try again.')
        return redirect('post_detail', pk=pk)
