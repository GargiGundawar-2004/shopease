# tests/test_api.py

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_response():
    response = client.get("/health")
    data = response.json()
    assert "status" in data