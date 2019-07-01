from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404


class UserRegistrationForm(UserCreationForm):
    '''Form used to register a new user'''
    username = forms.CharField(label = 'Your name', max_length = 100)
    password1 = forms.CharField(label = "Password",
                                widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Password Confirmation",
                                widget = forms.PasswordInput,
                                help_text = "Enter the same password as above, for verification.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email = email).exclude(username = username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords must match")
        return password2

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    '''Form to be used to log in users'''
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name" )

