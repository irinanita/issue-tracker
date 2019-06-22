from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import UserTicketVote
from tickets.models import Ticket
from django.contrib import messages

# Create your views here.
@login_required
def upvote(request,pk):
    ticket = get_object_or_404(Ticket,pk=pk) if pk else None
    user_ticket_vote = UserTicketVote.objects.all()
    user_ticket_vote = user_ticket_vote.filter(Q(ticketID=ticket.id) & Q(user=request.user)).count()
    print('ticket type',ticket.type)
    if user_ticket_vote==0:
        if ticket.type == "bug":
            user_vote=UserTicketVote(ticketID=ticket,user=request.user)
            user_vote.save()
            ticket.score+=1
            ticket.save()
            print(ticket.score,'current ticket score')
            messages.success(request,"You have successfully voted ")
        else:
            messages.success(request,"You need to pay first ")
            print('ticket score', ticket.score)
    else:
        messages.error(request,"You have alreaty voted for this")
    return redirect ("ticket_details",pk=ticket.id)
    
  
