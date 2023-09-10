FROM python:3

# Créez un répertoire de travail en dehors de /workspace
WORKDIR /app

# Mettez à jour les sources de paquets
RUN apt-get update

# Installez les dépendances nécessaires
RUN apt-get install -y libseccomp-dev

# Installez Podman
RUN apt-get install -y podman

# Copiez le fichier requirements.txt depuis le même répertoire que le Dockerfile
COPY requirements.txt requirements.txt

# Installez les dépendances Python
RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

# Installez python3 et python3-pip
RUN apt-get install -y python3 python3-pip

# Installez docker
RUN apt-get install -y docker.io

# Créez un environnement virtuel
RUN python3 -m venv venv

# Activez l'environnement virtuel
RUN /bin/bash -c "source venv/bin/activate"

# Installez Django
RUN pip install django

# Installez docker-compose en utilisant curl
RUN curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Copiez le reste du contenu
COPY . .

# Installez podman-compose
RUN apt-get install -y podman-compose

# Exécutez podman-compose avec un nom de projet spécifié
RUN podman-compose -p monprojet up

# Exposez le port 8000
EXPOSE 8000