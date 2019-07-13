from django.shortcuts import get_object_or_404
from tickets.models import Ticket


def cart_contents(request):
    '''
    Ensures that the cart contents are available to view when rendering every page
    It will request an existing cart or a blank dictionary if there is none
    '''
    cart = request.session.get('cart', {})

    cart_items = []
    total_value = 0

    for pk, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk = pk)
        total_value += 15
        cart_items.append({"pk": pk, "ticket": ticket})

    return {"cart_items": cart_items, "total_value": total_value}
