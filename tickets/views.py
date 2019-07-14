from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Ticket
from comments.models import Comment
from comments.forms import AddCommentForm
from .forms import AddTicketForm
from django.contrib.auth.decorators import login_required
import sweetify

# Create your views here.

def add_ticket(request):
    '''
    Create a view that allows us to create or edit a post
    (if the post ID is null or not)
    '''
    # ticket = get_object_or_404(Ticket,pk=pk) if pk else None
    if request.method == "POST":
        add_ticket_form = AddTicketForm(request.POST, request.FILES)
        if add_ticket_form.is_valid():

            ticket = add_ticket_form.save(commit = False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            ticket.user = request.user  # Set the user object here
            ticket.save()  # Now you can send it to DB
            sweetify.success(request, 'Ticket Added',  text = 'Your ticket was successfully added to the list')

            return redirect('ticketslist',ticket_type = 1)
    else:
        add_ticket_form = AddTicketForm()
    return render(request, 'addticket.html', {'add_ticket_form': add_ticket_form})


@login_required()
def ticketslist(request, ticket_type = None):
    tickets_list = Ticket.objects.all()
    if ticket_type == "2":
        tickets_list = tickets_list.filter(type__contains = "bug")
    if ticket_type == "3":
        tickets_list = tickets_list.filter(type__contains = "feature")

    paginator = Paginator(tickets_list, 2)
    page = request.GET.get('page')

    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tickets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tickets = paginator.page(paginator.num_pages)

    return render(request, 'ticketslist.html', {'tickets': tickets})


@login_required()
def ticket_details(request, pk):
    '''
    Will return a single ticket and all the information about it
    based on the Post ID (pk) and render it to ticketdetail.html template
    Or return 404 error if the post is not found
    '''
    ticket = get_object_or_404(Ticket, pk = pk) if pk else None
    add_comment_form = AddCommentForm()
    # get all comments where the ticket foreign key matches the current ticket pk
    comments = Comment.objects.filter(ticket = pk).order_by('-creation_date')

    if request.method == "POST":
        add_comment_form = AddCommentForm(request.POST)
        if add_comment_form.is_valid():

            comment = add_comment_form.save(commit = False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            ticket = Ticket.objects.get(id = pk)
            comment.ticket = ticket
            comment.user = request.user  # Set the user object here
            comment.save()  # Now you can send it to DB
            sweetify.success(request, 'Comment Added', text = 'Your comment was successfully added')
            add_comment_form = AddCommentForm()

    return render(request, "ticketdetails.html",
                  {'ticket': ticket, 'add_comment_form': add_comment_form, 'comments': comments})
