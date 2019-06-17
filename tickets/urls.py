from django.conf.urls import url
from .views import add_ticket,ticketslist,ticket_details
from upvoting.views import upvote

urlpatterns = [
    url(r'^addticket$',add_ticket,name="add_ticket"),
    url(r'^type/(?P<ticket_type>\w+)/$',ticketslist,name="ticketslist"),
    url(r'^details/(?P<pk>\d+)/$',ticket_details,name='ticket_details'),
    url(r'^upvote/(?P<pk>\d+)',upvote,name="upvote"),
]