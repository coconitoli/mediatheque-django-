from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_medias, name='liste_medias'),
    path('emprunter/<int:media_id>/<int:membre_id>/', views.emprunter_media, name='emprunter_media'),
    path('rendre/<int:media_id>/', views.rendre_media, name='rendre_media'),
]