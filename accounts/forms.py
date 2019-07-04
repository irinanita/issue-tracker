from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    '''Form used to register a new user'''
    username = forms.CharField(label = 'Username', max_length = 100)
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

    def clean_password2(self):
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

    YEARS = [x for x in range(1930, 2019)]
    birth_date = forms.DateField(widget = forms.SelectDateWidget(years = YEARS),initial="1970-06-21",required=False)
    class Meta:
        model = UserProfile
        fields = ("location","birth_date","avatar")
