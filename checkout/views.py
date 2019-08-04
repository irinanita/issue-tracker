from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineTicket
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket
from upvoting.models import UserTicketVote
import stripe
import sweetify

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():
            print('order form is valid')

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit = False)
            order.date = timezone.now()
            order.user = request.user
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                ticket = get_object_or_404(Ticket, pk = id)
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
                sweetify.error(request, 'Ooops', text = 'Your username or password is incorrect', persistent = 'Close')

            if customer.paid:
                for id, quantity in cart.items():
                    ticket = get_object_or_404(Ticket, pk = id)
                    user_vote = UserTicketVote(ticketID = ticket, user = request.user)
                    user_vote.save()
                    ticket.score += 1
                    ticket.save()
                    request.session['cart'] = {}
                    sweetify.success(request, 'Thank You!', text = 'You have successfully paid', )
                return redirect("ticket_details", pk = ticket.id)
            else:
                sweetify.error(request, 'Sorry', text = 'Unable to take payment', persistent = 'Close')
        else:
            print(payment_form.errors)
            sweetify.error(request, 'Sorry', text = 'We were unable to take a payment with that card!',
                           persistent = 'Close')
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


@login_required()
def checkout_buy_app(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():
            print('order form is valid')

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit = False)
            order.date = timezone.now()
            order.user = request.user
            order.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(49 * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                sweetify.error(request, 'Ooops', text = 'Your username or password is incorrect', persistent = 'Close')

            if customer.paid:

                return redirect("thank-you")
            else:
                sweetify.error(request, 'Sorry', text = 'Unable to take payment', persistent = 'Close')
        else:
            print(payment_form.errors)
            sweetify.error(request, 'Sorry', text = 'We were unable to take a payment with that card!',
                           persistent = 'Close')
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout-app.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


@login_required()
def thank_you(request):
    return render(request, 'thank-you.html')
