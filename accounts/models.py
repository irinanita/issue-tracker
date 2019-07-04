from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)
    avatar = models.ImageField(upload_to = "avatars", blank = True, null = True)

    def __str__(self):
        return "{0} -- Location: {1} -- Birthday: {2} ".format(self.user, self.location, self.birth_date)