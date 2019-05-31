from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    '''Form used to register a new user'''
    username = forms.CharField(label='Your name', max_length=100)
    password1=forms.CharField(label="Password",
                              widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Confirmation",
                              widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserLoginForm(forms.Form):
    '''Form to be used to log in users'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)        