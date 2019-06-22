from django.shortcuts import render,get_object_or_404
from tickets.models import Ticket

# Create your views here.
def view_cart(request):
  
    return render(request,'cart.html')
    