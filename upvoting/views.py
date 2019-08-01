from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import UserTicketVote
from tickets.models import Ticket
import sweetify


# Create your views here.
@login_required
def upvote(request, pk):
    ticket = get_object_or_404(Ticket, pk = pk) if pk else None
    user_ticket_vote = UserTicketVote.objects.all()
    user_ticket_vote = user_ticket_vote.filter(Q(ticketID = ticket.id) & Q(user = request.user)).count()
    if user_ticket_vote == 0:
        if ticket.type == "bug":
            user_vote = UserTicketVote(ticketID = ticket, user = request.user)
            user_vote.save()
            ticket.score += 1
            ticket.save()
            sweetify.success(request, 'You have successfully voted')
        else:
            cart = request.session.get('cart', {})
            cart[pk] = 1
            request.session['cart'] = cart
            return redirect("view_cart")
    else:
        sweetify.error(request, 'Sorry', text = 'You have already voted for this feature')
    return redirect("ticket_details", pk = ticket.id)
