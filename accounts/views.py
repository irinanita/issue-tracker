from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.

def registration(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = UserRegistrationForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/thanks/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {'registration_form': registration_form})