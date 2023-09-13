from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Classe, Etudiant, Filiere, Niveau
from django.contrib.auth.models import Group, User, Permission
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

# Create your views here.
excluded_models = [Group, User, LogEntry, Session, Permission, ContentType]


def sidebar_contents():
    excluded_models = [Group, User, LogEntry, Session, Permission, ContentType]
    admin_models = [model for model in apps.get_models() if model not in excluded_models]
    model_names_plural = [model._meta.verbose_name_plural for model in admin_models]
    return model_names_plural


def is_responsable(user):
    return user.groups.filter(name='responsable').exists()


def is_etudiant(user):
    return user.groups.filter(name='etudiant').exists()


@login_required(login_url='login')
@user_passes_test(is_responsable, login_url='login')
def index_responsable(request):
    sidebar_items = sidebar_contents()
    classes = Classe.objects.all();
    return render(request, "sekoly/index_responsable.html", {'model_names_plural': sidebar_items,'classes':classes})


@login_required(login_url='login')
@user_passes_test(is_etudiant, login_url='login')
def index_etudiant(request):
    return render(request, "sekoly/index_etudiant.html")


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_authenticated:
            login(request, user)
            groups = user.groups.all()
            print(groups)
            if groups.filter(name='etudiant').exists():
                return redirect('etudiant/')
            elif groups.filter(name='responsable').exists():
                return redirect('responsable/')

    # Si l'utilisateur n'est pas connecté ou la connexion a échoué, redirigez-le vers la page de connexion
    return redirect("login")

@login_required(login_url='login')
@user_passes_test(is_responsable, login_url='login')
def list_etudiants(request):
    etudiants = Etudiant.objects.all()
    sidebar_items = sidebar_contents()
    return render(request, "sekoly/list_etudiants.html", {'list_etudiants': etudiants, 'model_names_plural':sidebar_items})


@login_required(login_url='login')
@user_passes_test(is_responsable, login_url='login')
def classe_add(request):
    sidebar_items = sidebar_contents()
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()

    if request.method == 'POST':
        libelle = request.POST['libelle']
        filiere_id = request.POST['filiere']
        niveau_id = request.POST['niveau']
        
        filiere = Filiere.objects.get(pk=filiere_id)
        niveau = Niveau.objects.get(pk=niveau_id)

        existing_classe = Classe.objects.filter(libelle=libelle).first()
        
        if existing_classe:
            request.session['error_message'] = 'Une classe avec ce libellé existe déjà.'
            return redirect('index_responsable')
        
        nouvelle_classe = Classe(libelle=libelle, filiere=filiere, niveau=niveau)
        nouvelle_classe.save()

        return redirect('index_responsable')  

    return render(request, "sekoly/classe_add.html", {'model_names_plural': sidebar_items, 'filieres': filieres, 'niveaux': niveaux})