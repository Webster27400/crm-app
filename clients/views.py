# clients/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Task
from .forms import ClientForm
from .forms import ClientForm, TaskForm

def client_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients/client_list.html', context)

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.client = client
            new_task.save()
            return redirect('client_detail', pk=client.pk)
    else:
        task_form = TaskForm()

    tasks = client.tasks.all().order_by('due_date')

    context = {
        'client': client,
        'task_form': task_form,
        'tasks': tasks
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

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('client_detail', pk=task.client.pk)
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task  # Upewnij się, że ta linia jest obecna
    }
    return render(request, 'clients/task_form.html', context)

def task_archive(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_archived = True
    task.save()
    return redirect('client_detail', pk=task.client.pk)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    client_pk = task.client.pk
    task.delete()
    return redirect('client_detail', pk=client_pk)