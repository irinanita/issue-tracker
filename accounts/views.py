from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, ExtendedProfileForm
from .models import UserProfile
import sweetify


# Create your views here.

def registration(request):
    # is user is already authenticated
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        registration_form = UserRegistrationForm(request.POST)
        # check whether it's valid:
        if registration_form.is_valid():
            registration_form.save()
            user = authenticate(username = request.POST['username'],
                                password = request.POST['password1'])
            if user:
                login(request, user)
                UserProfile.objects.create(user = request.user)
                sweetify.success(request, 'You Registered', text = 'Your have successfully registered')
                return redirect(reverse('index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {'registration_form': registration_form})


def user_login(request):
    '''Return a login page'''
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username = request.POST['username'],
                                password = request.POST['password'])
            if user:
                login(request, user)
                sweetify.success(request, 'You Logged In', text = 'Your have successfully logged in')
                return redirect(reverse('index'))
            else:
                sweetify.error(request, 'Your username or password is incorrect', persistent = 'Close')

    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def user_logout(request):
    """A view that logs the user out and redirects back to the index page"""
    logout(request)
    sweetify.success(request, 'Logged Out', text = 'Your have successfully Logged Out')
    return redirect(reverse('index'))


def user_profile(request):
    current_user = request.user
    user_profile = UserProfile.objects.get(user = current_user.id)

    if request.method == "POST":
        profile_form = ExtendedProfileForm(instance = user_profile, data = request.POST, files = request.FILES)

        if profile_form.is_valid():
            profile_form.save()
            sweetify.success(request, 'Profile Updated', text = 'You have successfully updated your profile')
            return redirect('user_profile')
    else:
        profile_form = ExtendedProfileForm(instance = user_profile)

    return render(request, 'profile.html', {'profile_form': profile_form, 'user_profile': user_profile})


def delete_avatar(request):
    UserProfile.objects.get(user = request.user).avatar.delete(save = True)
    sweetify.success(request, 'Profile Updated', text = 'You have successfully deleted your avatar')
    return redirect('user_profile')
