from django.db import models
from tickets.models import Ticket
from django.conf import settings


# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length = 50, blank = False)
    phone_number = models.CharField(max_length = 20, blank = False)
    country = models.CharField(max_length = 40, blank = False)
    postcode = models.CharField(max_length = 20, blank = True)
    town_or_city = models.CharField(max_length = 40, blank = False)
    street_address1 = models.CharField(max_length = 40, blank = False)
    street_address2 = models.CharField(max_length = 40, blank = False)
    county = models.CharField(max_length = 40, blank = False)
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineTicket(models.Model):
    # Foreign Key relative to order
    order = models.ForeignKey(Order, null = False)
    # Foreign Key for the Product model we imported on top
    ticket = models.ForeignKey(Ticket, null = False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.ticket.id, self.ticket.title, self.ticket.type)
