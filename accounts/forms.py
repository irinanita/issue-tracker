from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    '''Form used to register a new user'''
    username = forms.CharField(label='Your name', max_length=100)
    password1=forms.CharField(label="Password",
                              widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Confirmation",
                              widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['email','username','password1','password2']