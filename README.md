# File-Downloader-Dockeris-

Ce projet Flask a été réalisé dans le cadre d’un test technique.  
Il permet de :
- Lister les fichiers disponibles
- Télécharger un fichier
- Tester l’API avec des endpoints simples
- Lancer l’app en local ou via Docker

---

##  Étapes de développement du projet

1. 
   - Création de la structure : `app/`, `routes.py`, `templates/`, etc.
   - Mise en place du serveur Flask minimal.

2. 
   - Création d’un dossier `files/` contenant des fichiers téléchargeables.
   - Implémentation de la route `/download/<filename>` pour les téléchargements.

3. 
   - Endpoint `/api/files` pour renvoyer la liste des fichiers en JSON.

4. 
   - Tests unitaires pour les routes principales.

5. 
   - Écriture d’un `Dockerfile` pour exécuter l'app facilement.

---
 Instructions d'installation

## 1. Cloner le projet

```bash
git clone https://github.com/ton-compte/ton-repo.git
cd ton-repo
## Créer un environnement virtuel

python -m venv venv

venv\Scripts\activate
## Installer les dépendances
pip install -r requirements.txt


## Lancer avec Docker

docker build -t file-downloader .
docker run -p 5000:5000 -v "${PWD}\files:/app/files" file-downloader

## Comment exécuter les tests
pytest
Assurez-vous d’avoir un fichier test.txt dans le dossier files/ avec le contenu suivant : contenu de test



