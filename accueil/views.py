from django.shortcuts import render

# from django.http import HttpResponse

from django.shortcuts import render
from datetime import date
from .forms import NomForm

def bonjour(request):
    message = "Bonjour, le monde de Django !"
    if request.method == 'POST':
        form = NomForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            message = f"Bonjour, {nom} !"
    else:
        form = NomForm()

    context = {
        'message': message,
        'date_du_jour': date.today(),
        'form': form
    }
    return render(request, 'accueil/index.html', context)