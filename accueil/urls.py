from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_taches, name='liste_taches'),  # Vue pour afficher la liste des tâches
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),  # Vue pour ajouter une tâche
]