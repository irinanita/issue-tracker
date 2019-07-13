from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Create your views here.
def view_cart(request):
    return render(request, 'cart.html')


def delete_product(request, pk):
    cart = request.session.get('cart', {})
    cart.pop(pk)
    request.session['cart'] = cart
    messages.success(request, "You have successfully removed one item from your cart")
    return redirect('view_cart')
