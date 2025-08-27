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

"""def dashboard(request):
    filter_by = request.GET.get('filter', 'status')
    valid_filters = ['status', 'country', 'offered_product', 'potential_market_share']

    if filter_by not in valid_filters:
        filter_by = 'status'

    filter_names = {
        'status': 'Status',
        'country': 'Country',
        'offered_product': 'Offered Product',
        'potential_market_share': 'Potential Market Share'
    }

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
        'filter_by': filter_by,
        'filter_name': filter_names.get(filter_by, 'Status')
    }
    return render(request, 'clients/dashboard.html', context)"""

# clients/views.py
# ... (pozostałe importy)

def dashboard(request):
    filter_by = request.GET.get('filter', 'status')
    valid_filters = ['status', 'country', 'offered_product', 'potential_market_share']
    
    if filter_by not in valid_filters:
        filter_by = 'status'

    # Dodatkowe dane dla tekstu raportu
    filter_names = {
        'status': 'Status',
        'country': 'Country',
        'offered_product': 'Offered Product',
        'potential_market_share': 'Potential Market Share'
    }

    counts = {}
    roadblock_counts = {}

    for item in Client.objects.all():
        # Dane dla pierwszego wykresu (filtrowane dynamicznie)
        value = getattr(item, filter_by)
        
        if filter_by == 'offered_product':
            value = item.get_offered_product_display()
        elif filter_by == 'potential_market_share':
            value = f"{value}%"
        
        counts[value] = counts.get(value, 0) + 1

        # Dane dla drugiego wykresu (statyczne, tylko dla statusu On Hold)
        if item.status == 'On Hold' and item.reason_for_roadblock:
            roadblock = item.reason_for_roadblock
            roadblock_counts[roadblock] = roadblock_counts.get(roadblock, 0) + 1

    context = {
        'counts': counts,
        'filter_by': filter_by,
        'roadblock_counts': roadblock_counts,
        'filter_name': filter_names.get(filter_by, 'Status') # Make sure this line is here
    }
    return render(request, 'clients/dashboard.html', context)