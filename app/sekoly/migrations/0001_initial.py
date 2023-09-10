# Generated by Django 4.2.5 on 2023-09-10 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('idClasse', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coeff',
            fields=[
                ('idCoeff', models.AutoField(primary_key=True, serialize=False)),
                ('valeur', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('idFiliere', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('idMatiere', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('idNiveau', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('idEtudiant', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('dateDeNaissance', models.DateField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.classe')),
            ],
        ),
        migrations.CreateModel(
            name='CoeffMatiereFiliere',
            fields=[
                ('idCoeffMatiereFiliere', models.AutoField(primary_key=True, serialize=False)),
                ('coefficient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.coeff')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.filiere')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='ClasseMatiere',
            fields=[
                ('idClasseMatiere', models.AutoField(primary_key=True, serialize=False)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.classe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.filiere'),
        ),
        migrations.AddField(
            model_name='classe',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekoly.niveau'),
        ),
    ]
