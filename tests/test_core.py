from fastapi.testclient import TestClient
from src.main import app

cliente = TestClient(app)

def test_root():
  response = cliente.get('/')
  assert response.status_code == 200
  assert response.json() == {'mensaje':'Hola mundo nojoda!!'}