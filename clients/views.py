# clients/views.py
from django.shortcuts import render, get_object_or_404
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/client_list.html', context)

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    context = {
        'client': client
    }
    return render(request, 'clients/client_detail.html', context)