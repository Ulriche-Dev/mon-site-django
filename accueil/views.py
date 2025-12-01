from django.shortcuts import render, redirect
from .forms import TacheForm
from .models import Tache
from datetime import date, datetime

def liste_taches(request):
    """
    Vue pour afficher la liste des tâches et le formulaire d'ajout.

    Arguments :
        request (HttpRequest) : L'objet de requête HTTP.

    Retourne :
        HttpResponse : La réponse HTTP contenant le rendu de la page d'accueil.
    """
    # current_hour = datetime.now().hour
    # if current_hour < 12:
    #     message = "Bon matin !"
    # else:
    #     message = "Bon après-midi !"

    form = TacheForm()
    taches = Tache.objects.all().order_by('titre')

    context = {
        # 'message': message,
        # 'date_du_jour': date.today(),
        'form': form,
        'taches': taches
    }
    return render(request, 'accueil/index.html', context)

def ajouter_tache(request):
    """
    Vue pour gérer l'ajout d'une nouvelle tâche.

    Arguments :
        request (HttpRequest) : L'objet de requête HTTP.

    Retourne :
        HttpResponse : Redirige vers la vue liste_taches après ajout.
    """
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('liste_taches')