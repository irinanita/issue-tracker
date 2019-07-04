from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineTicket
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket
from upvoting.models import UserTicketVote
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if payment_form.is_valid():
            print('order form is valid')
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                ticket = get_object_or_404(Ticket, pk=id)
                total += 15
                order_line_ticket = OrderLineTicket(
                    order = order, 
                    ticket = ticket, 
                    )
                order_line_ticket.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                request.session['cart'] = {}
                messages.success(request, "You have successfully paid", extra_tags="ticket-update")
                user_vote=UserTicketVote(ticketID=ticket,user=request.user)
                user_vote.save()
                ticket.score+=1
                ticket.save()
                return redirect("ticket_details",pk=ticket.id)
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})