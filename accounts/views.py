from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm
from .models import UserProfile


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
                messages.success(request, "You have successfully logged in")
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
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def user_logout(request):
    """A view that logs the user out and redirects back to the index page"""
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def user_profile(request):
    current_user = request.user
    user = User.objects.get(pk = current_user.id)
    user_form = UserRegistrationForm(instance=user)
    user_form.fields['username'].widget.attrs['readonly'] = True
    user_form.fields['username'].required = False
    profile_form = ProfileForm(instance=user)

    return render(request, 'profile.html',{'user_form':user_form,'profile_form':profile_form})

