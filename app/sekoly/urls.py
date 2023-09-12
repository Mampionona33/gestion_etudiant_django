from django.urls import path

from . import views

urlpatterns = [
    path("responsable/etudiants/", views.list_etudiants, name='etudiants'),
    path("responsable/classes/", views.list_etudiants, name='classes'),
    path("responsable/filieres/", views.list_etudiants, name='filieres'),
    path("responsable/niveaus/", views.list_etudiants, name='niveaus'),
    path("responsable/matieres/", views.list_etudiants, name='matieres'),
    path("responsable/coeffs/", views.list_etudiants, name='coeffs'),
    path("responsable/coeff-atiere-filieres/", views.list_etudiants,
         name='coeff matiere filieres'),
    path("responsable/classe-matieres/",
         views.list_etudiants, name='classe matieres'),
    path("responsable/", views.index_responsable, name='index_responsable'),
    path("etudiant/", views.index_etudiant, name='index_etudiant'),
    path("", views.index, name="index"),
]
