from django.shortcuts import render
from django.db.models import Q
from tickets.models import Ticket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# Will return true if both conditions are met
def is_valid_query_param(param):
    return param != '' and param is not None


def search(request):
    # fetch all tickets unfiltered
    query_set = Ticket.objects.all()
    # check if the submitted form was a filter/search or a reset
    if request.GET.get('search') != '' and request.GET.get('search') is not None:
        query_keyword = request.GET.get('q')
        query_status = request.GET.get('status')
        query_label = request.GET.get('label')
        query_sort = request.GET.get('sort')

        if is_valid_query_param(query_keyword):
            # Searching whether keywords are present in the title or in the description
            query_set = query_set.filter(
                Q(title__icontains = query_keyword) | Q(description__icontains = query_keyword)).distinct()
        if is_valid_query_param(query_status):
            query_set = query_set.filter(status__icontains = query_status)
        if is_valid_query_param(query_label):
            query_set = query_set.filter(label__icontains = query_label)
        if is_valid_query_param(query_sort):
            if query_sort == "recently added on top":
                query_set = query_set.order_by('-creation_date')
            if query_sort == "oldest on top":
                query_set = query_set.order_by('creation_date')
            if query_sort == "best score on top":
                query_set = query_set.order_by('-score')
    paginator = Paginator(query_set, 2)
    page = request.GET.get('page')
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    filter = {'keyword': query_keyword, 'status': query_status,
              'label': query_label, 'sort': query_sort}

    return render(request, "ticketslist.html", {"tickets": tickets, "filter": filter})
