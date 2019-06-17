from django.db import models
from tickets.models import Ticket
from django.conf import settings

# Create your models here.
class UserTicketVote(models.Model):
    ticketID=models.ForeignKey('tickets.Ticket')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    #auto_now and auto_now_add imply the field is not user-editable and must always get set to this value
    
    def __str__(self):
        return "User: {0} -- Ticket: {1} ".format( self.user, self.ticketID )
