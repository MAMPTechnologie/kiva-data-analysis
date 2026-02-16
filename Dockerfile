# Utilise une version stable et légère de Python
FROM python:3.11-slim

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Installe les dépendances système nécessaires (si besoin de compiler certains outils)
RUN apt-get update && apt-get install -y build-essential --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copie le fichier des dépendances et installe-les
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt
# On ne copie pas 'data' ici pour garder l'image légère, on utilisera un "Volume"
COPY scripts/ /app/scripts/

# Commande par défaut (garde le conteneur ouvert pour que tu puisses travailler dedans)
CMD ["tail", "-f", "/dev/null"]