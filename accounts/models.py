from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    birth_date = models.DateField(blank = True, null = True)
    avatar = models.ImageField(upload_to = "avatars", blank = True)
    country = CountryField(blank = True, null = False)
    bio = models.TextField(max_length = 300, blank = True, null = False)

    def __str__(self):
        return "{0} -- Location: {1}".format(self.user, self.country)
