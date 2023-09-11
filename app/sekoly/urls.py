from django.urls import path

from . import views

urlpatterns = [
    path("responsable/",views.index_responsable, name='index_responsable'),
    path("etudiant/",views.index_etudiant, name='index_etudiant'),
    path("", views.index, name="index"),
]
