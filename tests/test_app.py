import os
import tempfile
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    test_dir = tempfile.TemporaryDirectory()
    # Crée un fichier de test temporaire
    test_file_path = os.path.join(test_dir.name, "test.txt")
    with open(test_file_path, "w") as f:
        f.write("contenu de test")

    app = create_app()
    app.config["TESTING"] = True
    app.config["FILES_DIR"] = test_dir.name

    with app.test_client() as client:
        yield client

    test_dir.cleanup()

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Fichiers disponibles" in response.data

def test_api_files(client):
    response = client.get("/api/files")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "files" in json_data
    assert "test.txt" in json_data["files"]

def test_file_download(client):
    response = client.get("/download/test.txt") 
    print(repr(response.data))

    assert response.status_code == 200
    assert response.data.strip() == b"contenu de test"


