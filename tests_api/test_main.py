# tests_api/test_main.py
import os
import sys
import pytest
from fastapi.testclient import TestClient
from dotenv import load_dotenv

# Ajouter le chemin du dossier racine du projet
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Api.main import app

# Charger les variables d'environnement pour les tests
load_dotenv(dotenv_path='BDD/credentials.env')

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "password": "testpassword"})
    print(f"test_create_user status code {response.status_code}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    print("test_create_user passed")

def test_login():
    response = client.post("/login", data={"username": "testuser", "password": "testpassword"})
    print(f"test_login status code {response.status_code}")
    assert response.status_code == 200
    assert "Connexion réussie" in response.json()["message"]
    print("test_login passed")

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description", "due_date": "2024-06-06", "completed": False})
    print(f"test_create_task status code {response.status_code}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    print("test_create_task passed")
