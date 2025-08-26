# clients/views.py
from django.shortcuts import render
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/client_list.html', context)