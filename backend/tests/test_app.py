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

def test_game_start_success(client):
    payload = {
        "gameDifficultyLevel": "normal",
        "userId": 1  # Assuming user ID 1 exists in test data
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post('/api/game/start', json=payload, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 'success'
    assert 'game_id' in data
    assert 'crossword' in data