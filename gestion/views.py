import logging
from django.shortcuts import render, redirect
from .models import Media, Membre

logger = logging.getLogger(__name__)

def liste_medias(request):
    """Affiche tous les médias disponibles et empruntés."""
    medias = Media.objects.all()
    return render(request, 'gestion/liste_medias.html', {'medias': medias})

def emprunter_media(request, media_id, membre_id):
    media = Media.objects.get(id=media_id)
    membre = Membre.objects.get(id=membre_id)

    # 1. Règle : Vérifier si le membre est bloqué
    if membre.bloque:
        logger.warning("Membre bloqué essaie d'emprunter : %s", membre.name)
        return render(request, 'gestion/erreur.html', {'message': "Votre compte est bloqué."})

    # 2. Règle : Vérifier la limite des 3 emprunts
    nb_emprunts = Media.objects.filter(emprunteur=membre).count()
    if nb_emprunts >= 3:
        logger.warning("Quota dépassé pour %s (déjà %s emprunts)", membre.name, nb_emprunts)
        return render(request, 'gestion/erreur.html', {'message': "Quota de 3 emprunts maximum atteint."})

    # 3. Règle : Vérifier si le média est déjà pris
    if not media.disponible:
        logger.warning("Média déjà emprunté : %s", media.name)
        return render(request, 'gestion/erreur.html', {'message': "Ce média n'est pas disponible."})

    # Validation de l'emprunt
    media.disponible = False
    media.emprunteur = membre
    media.save()
    logger.info("Succès : '%s' emprunté par '%s'", media.name, membre.name)

    return redirect('liste_medias')

def rendre_media(request, media_id):
    media = Media.objects.get(id=media_id)

    if media.disponible:
        logger.warning("Tentative de retour d'un média non emprunté : %s", media.name)
        return render(request, 'gestion/erreur.html', {'message': "Ce média est déjà présent en rayon."})

    ancien_emprunteur = media.emprunteur.name if media.emprunteur else "Inconnu"

    media.disponible = True
    media.emprunteur = None
    media.save()
    logger.info("Média '%s' rendu par '%s'", media.name, ancien_emprunteur)

    return redirect('liste_medias')