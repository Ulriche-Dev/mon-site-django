from django.test import TestCase
from .models import Tache

class TacheModelTest(TestCase):

    def test_str_method(self):
        # Créer une instance de Tache
        tache = Tache.objects.create(titre="Apprendre Django", termine=False)
        # Vérifier que __str__ retourne le titre
        self.assertEqual(str(tache), "Apprendre Django")
