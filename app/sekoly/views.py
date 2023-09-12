from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Classe
# Create your views here.

def is_responsable(user):
    return user.groups.filter(name='responsable').exists()

def is_etudiant(user):
    return user.groups.filter(name='etudiant').exists()

@login_required(login_url='login')
@user_passes_test(is_responsable, login_url='login')
def index_responsable(request):
    class_list = Classe.objects.all()
    return render(request, "sekoly/index_responsable.html",{'class_list': class_list})

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


