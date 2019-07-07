from django.shortcuts import render
from tickets.models import Ticket


# Create your views here.
def index(request):
    '''
    A view that displays our landing page.
    For logged users it displays dashboards
    '''
    tickets_list = Ticket.objects.all()
    bugs_list = tickets_list.filter(type__contains = "bug").order_by('-score')[:3]
    features_list = tickets_list.filter(type__contains = "feature").order_by('-score')[:3]
    latest_tickets = tickets_list.filter(type__contains = "bug").order_by('-creation_date')[:3]

    return render(request, 'index.html',
                  {"bugs_list": bugs_list, "features_list": features_list, "latest_tickets": latest_tickets})
