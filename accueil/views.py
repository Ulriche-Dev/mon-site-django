from django.shortcuts import render

# from django.http import HttpResponse

from django.shortcuts import render
from datetime import date, datetime
from .forms import NomForm

def bonjour(request):
    current_hour = datetime.now().hour
    if current_hour < 12:
        message = "Bon matin !"
    else:
        message = "Bon après-midi !"

    if request.method == 'POST':
        form = NomForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            message = f"{message} {nom} !"
    else:
        form = NomForm()

    # Liste de tâches
    taches = [
        "Apprendre Django",
        "Créer un projet web",
        "Faire une pause café",
        "Boire un café",
        "Déployer l'application"
    ]

    context = {
        'message': message,
        'date_du_jour': date.today(),
        'form': form,
        'taches': taches
    }
    return render(request, 'accueil/index.html', context)