from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Ticket
from .forms import AddTicketForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def add_ticket(request):
    current_user = request.user
    print (current_user.id,type(current_user.id))
    '''
    Create a view that allows us to create or edit a post
    (if the post ID is null or not)
    '''
    #ticket = get_object_or_404(Ticket,pk=pk) if pk else None
    if request.method == "POST":
        add_ticket_form = AddTicketForm(request.POST,request.FILES)
        if add_ticket_form.is_valid():
            
            ticket = add_ticket_form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            ticket.user = request.user # Set the user object here
            ticket.save() # Now you can send it to DB
            
            messages.success(request,"ticket added")
            return redirect(reverse('index'))
    else:
        add_ticket_form = AddTicketForm()
    return render(request, 'addticket.html' , {'add_ticket_form': add_ticket_form} )

@login_required()    
def ticketslist(request):
    tickets = Ticket.objects.all()
    return render(request,'ticketslist.html',{'tickets':tickets})
