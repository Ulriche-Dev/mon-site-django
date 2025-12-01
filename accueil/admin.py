from django.contrib import admin
from .models import Tache

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('titre', 'termine')  # Affiche ces champs dans la liste des tâches
    list_filter = ('termine',)          # Ajoute un filtre pour le champ 'termine'
    search_fields = ('titre',)          # Ajoute une barre de recherche pour le champ 'titre'