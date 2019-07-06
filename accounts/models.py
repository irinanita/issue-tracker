from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)
    avatar = models.ImageField(upload_to = "avatars", default='avatars/default.png')
    country = CountryField(blank = True, null = False)
    bio = models.TextField(max_length = 300, blank = True, null = False)

    def __str__(self):
        return "{0} -- Location: {1} -- Birthday: {2} ".format(self.user, self.location, self.birth_date)
