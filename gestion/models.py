from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=100)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Membre', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Livre(Media):
    auteur = models.CharField(max_length=100)

class Dvd(Media):
    realisateur = models.CharField(max_length=100)

class Cd(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Membre(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name