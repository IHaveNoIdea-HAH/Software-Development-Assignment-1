import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_welcome(client):
    response = client.get('/api/game/welcome')
    assert response.status_code == 200
    assert b"welcome" in response.data.lower()

