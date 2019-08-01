from django.shortcuts import render, redirect
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
    query_type = request.GET.get('search')
    # check if the submitted form was a filter/search or a reset
    if is_valid_query_param(query_type) and query_type != 'reset':
        query_keyword = request.GET.get('q')
        query_status = request.GET.get('status')
        query_label = request.GET.get('label')
        query_sort = request.GET.get('sort')

        filter = {'keyword': query_keyword, 'status': query_status,
                  'label': query_label, 'sort': query_sort, 'type': query_type}

        if query_type == 'bug' or query_type == 'feature':
            query_set = query_set.filter(type__icontains = query_type)

        if is_valid_query_param(query_keyword):
            # Searching whether keywords are present in the title or in the description
            query_set = query_set.filter(
                Q(title__icontains = query_keyword) | Q(description__icontains = query_keyword)).distinct()
        if is_valid_query_param(query_status):
            query_set = query_set.filter(status__icontains = query_status)
        if is_valid_query_param(query_label):
            query_set = query_set.filter(label__icontains = query_label)
        if query_set.count() == 0:
            filter = {}
        if is_valid_query_param(query_sort):
            if query_sort == "recently added on top":
                query_set = query_set.order_by('-creation_date')
            if query_sort == "oldest on top":
                query_set = query_set.order_by('creation_date')
            if query_sort == "best score on top":
                query_set = query_set.order_by('-score')
    else:
        return redirect('ticketslist')

    paginator = Paginator(query_set, 4)
    page = request.GET.get('page')
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    return render(request, "ticketslist.html", {"tickets": tickets, "filter": filter})
