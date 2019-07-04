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
            messages.success(request,"You have successfully voted ", extra_tags="ticket-update")
        else:
            cart=request.session.get('cart',{})
            cart[pk] = 1
            request.session['cart'] = cart
            messages.success(request,"In order to upvote a feature a small contribution of 15 EUR per feature is required. Remember you can only vote once")
            return redirect ("view_cart")
    else:
        messages.error(request,"You have alreaty voted for this", extra_tags="ticket-update")
    return redirect ("ticket_details",pk=ticket.id)
    
  