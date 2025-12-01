from django.db import models

class Tache(models.Model):
    """
    Modèle représentant une tâche.

    Attributs :
        - titre (CharField) : Le titre de la tâche, limité à 200 caractères.
        - termine (BooleanField) : Indique si la tâche est terminée (par défaut : False).
    """
    titre = models.CharField(max_length=200)
    termine = models.BooleanField(default=False)

    def __str__(self):
        """
        Retourne une représentation textuelle de la tâche.

        Retourne :
            str : Le titre de la tâche.
        """
        return self.titre
