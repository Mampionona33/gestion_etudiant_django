from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.


# def index(request):
#     return render(request, "sekoly/index.html")

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Connectez l'utilisateur
            return render(request, "sekoly/index.html")
    
    # Si l'utilisateur n'est pas connecté ou la connexion a échoué, redirigez-le vers la page de connexion
    return redirect("login")


