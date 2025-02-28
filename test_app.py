import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, CI/CD!"
