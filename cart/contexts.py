from django.shortcuts import get_object_or_404
from tickets.models import Ticket

def cart_contents(request):
    '''
    Ensures that the cart contents are available to view when rendering every page
    It will request an existing cart or a blank dictionary if there is none
    '''
    cart = request.session.get('cart',{})
    
    cart_items=[]
    
    for pk, quantity in cart.items():
        ticket=get_object_or_404(Ticket,pk=pk)
        cart_items.append({"pk":pk,"ticket":ticket})
        print('cart items',cart_items)
    return {"cart_items":cart_items}