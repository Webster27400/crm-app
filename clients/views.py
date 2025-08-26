# clients/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

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

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    
    context = {
        'form': form
    }
    return render(request, 'clients/client_form.html', context)

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    
    context = {
        'form': form,
        'client': client
    }
    return render(request, 'clients/client_form.html', context)

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    
    context = {
        'client': client
    }
    return render(request, 'clients/client_confirm_delete.html', context)

def dashboard(request):
    filter_by = request.GET.get('filter', 'status')
    valid_filters = ['status', 'country', 'offered_product', 'potential_market_share']

    if filter_by not in valid_filters:
        filter_by = 'status'

    counts = {}
    for item in Client.objects.all():
        value = getattr(item, filter_by)

        if filter_by == 'offered_product':
            # Pobieramy pełną nazwę produktu
            value = item.get_offered_product_display()
        elif filter_by == 'potential_market_share':
            # Dodajemy znak % do wartości
            value = f"{value}%"

        counts[value] = counts.get(value, 0) + 1

    context = {
        'counts': counts,
        'filter_by': filter_by
    }
    return render(request, 'clients/dashboard.html', context)