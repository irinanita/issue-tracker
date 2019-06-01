from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Ticket
from .forms import AddTicketForm

# Create your views here.

def add_ticket(request):
    '''
    Create a view that allows us to create or edit a post
    (if the post ID is null or not)
    '''
    #ticket = get_object_or_404(Ticket,pk=pk) if pk else None
    if request.method == "POST":
        add_ticket_form = AddTicketForm(request.POST,request.FILES)
        if add_ticket_form.is_valid():
            obj=Ticket() #get the Ticket object that we need to save the input
            obj.title=add_ticket_form.cleaned_data['title']
            obj.description=add_ticket_form.cleaned_data['description']
            obj.type=add_ticket_form.cleaned_data['type']
            obj.label=add_ticket_form.cleaned_data['label']
            obj.image=add_ticket_form.cleaned_data['image']
            obj.save()
            messages.success(request,"ticket added")
            return redirect(reverse('index'))
    else:
        add_ticket_form = AddTicketForm()
    return render(request, 'addticket.html' , {'add_ticket_form': add_ticket_form} )    
