from django.db import models
from django.conf import settings


# Create your models here.
class Comment(models.Model):
    ticket = models.ForeignKey('tickets.Ticket')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    content = models.TextField(blank = False, null = False)
    creation_date = models.DateTimeField(auto_now_add = True)

    # auto_now and auto_now_add imply the field is not user-editable and must always get set to this value

    def __str__(self):
        return "{0} -- Type: {1} -- Status: {2} ".format(self.ticket, self.user, self.creation_date)
