from flask import Blueprint, render_template, send_from_directory, jsonify
from urllib.parse import unquote
import os

main = Blueprint('main', __name__)

# Utiliser un chemin absolu pour s'assurer que le dossier 'files' est bien trouvé
FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'files')

@main.route("/")
def index():
    files = os.listdir(FILES_DIR)
    return render_template("index.html", files=files)

# Utiliser <path:filename> pour autoriser les noms avec des espaces ou / 
@main.route("/download/<path:filename>")
def download_file(filename):
    filename = unquote(filename)  # Décoder les espaces, %20, etc.
    return send_from_directory(FILES_DIR, filename, as_attachment=True)

@main.route("/api/files")
def api_files():
    files = os.listdir(FILES_DIR)
    return jsonify({"files": files})


@main.app_template_filter('get_icon')
def get_icon(filename):
    ext = filename.lower().split('.')[-1]
    if ext in ['pdf']:
        return "📄"
    elif ext in ['jpg', 'jpeg', 'png', 'gif']:
        return "🖼️"
    elif ext in ['zip', 'rar', ]:
        return "📦"
    elif ext in ['txt', 'md']:
        return "📑"
  
    else:
        return "📁"
