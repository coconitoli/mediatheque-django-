from django.test import TestCase
from .models import Livre, Membre

class MediathequeTestCase(TestCase):
    def setUp(self):
        # Création des données de test initiales
        self.membre = Membre.objects.create(name="Vladimir", bloque=False)
        self.livre = Livre.objects.create(name="1984", disponible=True)

    def test_creation_membre(self):
        """Vérifie qu'un membre est bien créé."""
        self.assertEqual(self.membre.name, "Vladimir")
        self.assertFalse(self.membre.bloque)

    def test_disponibilite_livre(self):
        """Vérifie qu'un livre créé est disponible par défaut."""
        self.assertTrue(self.livre.disponible)