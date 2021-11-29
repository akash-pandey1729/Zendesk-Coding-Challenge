import requests
from django.shortcuts import render
from django.core.paginator import Paginator

length = 0
auth = False
tickets = []

# Create your views here.

def fetchTickets(username, subdomain, password):
    global tickets, length, auth

    response = requests.get(f'https://{subdomain}.zendesk.com/api/v2/requests.json', auth = (f'{username}/token', password)).json()
    
    if 'error' in response:
        pass
    else:
        auth = True
        tickets = response['requests']

        while response['next_page']:
            response = requests.get(response['next_page'], auth = (f'{username}/token', password)).json()
            tickets.extend(response['requests'])

        for index, ticket in enumerate(tickets):
            length += 1
            ticket['index'] = index

def home(request):
    if not auth:
        context = {
            'title' : 'home',
            'auth' : auth,
        }
    else:     
        paginator = Paginator(tickets, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'title' : 'home',
            'auth' : auth,
            'length' : length,
            'page_obj' : page_obj,
            'tickets' : page_obj.object_list,
        }

    return render(request, 'ticket/home.html', context)

def about(request):
    context = {
        'title' : 'about',
        'auth' : auth,
    }

    return render(request, 'ticket/about.html', context)

def individual_ticket(request, pk):
    context = {
            'title' : 'ticket',
            'auth' : auth,
            'ticket' : tickets[pk],
        }

    return render(request, 'ticket/individual_ticket.html', context)