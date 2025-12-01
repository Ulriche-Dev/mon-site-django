from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bonjour, name='bonjour'),  # Route pour la vue bonjour
]