from django.shortcuts import render, redirect
import sweetify


# Create your views here.
def view_cart(request):
    return render(request, 'cart.html')


def delete_product(request, pk):
    cart = request.session.get('cart', {})
    cart.pop(pk)
    request.session['cart'] = cart
    sweetify.success(request, 'Item removed', text = 'Your have successfully removed a ticket from your cart')
    return redirect('view_cart')
