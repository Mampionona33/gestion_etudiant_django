from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Etudiant(models.Model):
    idEtudiant = models.AutoField(primary_key=True, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    dateDeNaissance = models.DateField()
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Classe(models.Model):
    idClasse = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255)
    filiere = models.ForeignKey('Filiere', on_delete=models.CASCADE)
    niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class ClasseMatiere(models.Model):
    idClasseMatiere = models.AutoField(primary_key=True)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)

class Filiere(models.Model):
    idFiliere = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle

class Niveau(models.Model):
    idNiveau = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle

class Matiere(models.Model):
    idMatiere = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle

class Coeff(models.Model):
    idCoeff = models.AutoField(primary_key=True)
    valeur = models.FloatField()

    def __str__(self):
        return str(self.valeur)

class CoeffMatiereFiliere(models.Model):
    idCoeffMatiereFiliere = models.AutoField(primary_key=True)
    coefficient = models.ForeignKey('Coeff', on_delete=models.CASCADE)
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    filiere = models.ForeignKey('Filiere', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.coefficient} / {self.matiere} / {self.filiere}"
