from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile
from django.core.files.images import get_image_dimensions


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
    """Form to be used to log in users"""
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


class ExtendedProfileForm(forms.ModelForm):
    YEARS = [x for x in range(1930, 2019)]
    birth_date = forms.DateField(widget = forms.SelectDateWidget(years = YEARS), initial = "1970-06-21",
                                 required = False)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 250
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image')

            # validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar

    class Meta:
        model = UserProfile
        fields = ("country", "birth_date", "bio", "avatar")
