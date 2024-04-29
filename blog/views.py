import profile

from django.contrib.auth.models import User
from django.db import OperationalError
from django.core.exceptions import ValidationError
from django.http import Http404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from profiles.models import Profile
from .forms import BlogPostForm
from .models import BlogPost, Tag


def index(request):
    return render(request, 'index.html')


def post_list(request):
    try:
        posts = BlogPost.objects.all().order_by('-publication_date')
        #post = get_object_or_404(BlogPost)
        tags = Tag.objects.all()
        return render(request, 'post_list.html', {'posts': posts, 'tags': tags})
    except OperationalError as e:
        messages.error(request, 'Database error occurred while fetching the post list. Please try again.')
        return redirect('post_list')


def post_detail(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        return render(request, 'post_detail.html', {'post': post})
    except Http404:
        messages.error(request, 'Post does not exist.')
        return redirect('post_list')


@login_required
def post_create(request):
    tags = Tag.objects.all()
    try:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = Profile.user.username  # Set the author field
                post.save()
                form.save_m2m()  # Save many-to-many relationships
                messages.success(request, f'Post "{post.title}" has been successfully created!')
                return redirect('post_detail', pk=post.pk)
        else:
            form = BlogPostForm()
        return render(request, 'post_edit.html', {'form': form, 'tags': tags})
    except ValidationError as e:
        messages.error(request, f'Validation error occurred: {e}')
        return redirect('post_create')


@login_required
def post_edit(request, pk):
    tags = Tag.objects.all()
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, f'Post "{post.title}" has been successfully updated!')
                return redirect('post_detail', pk=post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})
    except ValidationError as e:
        messages.error(request, f'Validation error occurred: {e}')
        return redirect('post_edit', pk=pk)


@login_required
def post_delete(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        post.delete()
        messages.success(request, 'Post has been successfully deleted!')
        return redirect('post_list')
    except OperationalError as e:
        messages.error(request, 'Database error occurred while deleting the post. Please try again.')
        return redirect('post_detail', pk=pk)


def about(request):
    return render(request, 'about.html')


def navbar(request):
    return render(request, 'navbar.html')