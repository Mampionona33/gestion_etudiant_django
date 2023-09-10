from django.contrib import admin

from .models import Etudiant, Classe, ClasseMatiere, Filiere, Niveau, Matiere, Coeff, CoeffMatiereFiliere

# Enregistrez vos modèles ici.
admin.site.register(Etudiant)
admin.site.register(Classe)
admin.site.register(ClasseMatiere)
admin.site.register(Filiere)
admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Coeff)
admin.site.register(CoeffMatiereFiliere)
