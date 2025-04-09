from django.shortcuts import render, redirect
from .models import Produkt
from .forms import ProduktForm
from django.contrib.auth.decorators import login_required

def produkt_list(request):
    produkty = Produkt.objects.all().order_by('-data_dodania')
    return render(request, 'produkty/produkt_list.html', {'produkty': produkty})

@login_required
def produkt_create(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produkt_list')
    else:
        form = ProduktForm()
    return render(request, 'produkty/produkt_create.html', {'form': form})
