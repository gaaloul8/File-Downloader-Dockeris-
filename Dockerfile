# Utilise une image Python officielle
FROM python:3.11-slim

# Crée le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers nécessaires dans le conteneur
COPY . /app

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Spécifie le port exposé
EXPOSE 5000

# Définir la variable d’environnement pour le répertoire de fichiers
ENV FILES_DIR=files

# Lancer l'application
CMD ["python", "run.py"]
