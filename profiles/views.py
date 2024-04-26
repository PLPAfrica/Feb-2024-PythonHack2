from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  # Import authenticate as well
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render

from profiles.forms import CustomUserCreationForm, UserProfileForm
from profiles.models import Profile


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # Check if a profile already exists for the user
            profile, created = Profile.objects.get_or_create(user=user)
            # If profile already exists, update it with the new data
            if not created:
                profile.location = profile_form.cleaned_data['location']
                profile.profile_picture = profile_form.cleaned_data['profile_picture']
                profile.job_title = profile_form.cleaned_data['job_title']
                profile.skills = profile_form.cleaned_data['skills']
                profile.save()
            authenticated_user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect('index')  # Change 'index' to your desired URL name
        else:
            # Form is not valid, display error messages
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            for field, errors in profile_form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('index')  # Change 'home' to your desired URL name
        # Authentication failed, display error message
        messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  # Change 'login' to your login URL


@login_required
def profile_manager(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'profile_manager.html', context)
