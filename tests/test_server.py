import pytest
from flask import Flask
from server.app import app, db
from server.models import Track

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_tracks_empty(client):
    response = client.get('/api/tracks')
    assert response.status_code == 200
    assert response.json == []

def test_add_track(client):
    data = {
        'title': 'Test Track',
        'artist': 'Test Artist',
        'genre': 'Rock',
        'duration': 180
    }
    
    response = client.post('/api/track', json=data)
    assert response.status_code == 201
    assert response.json['title'] == 'Test Track'
    assert response.json['artist'] == 'Test Artist'
    
    # Проверяем, что трек действительно добавлен
    response = client.get('/api/tracks')
    assert len(response.json) == 1
    assert response.json[0]['title'] == 'Test Track'

def test_get_stats(client):
    # Добавляем тестовые данные
    tracks = [
        Track(title='Track 1', artist='Artist 1', genre='Rock', duration=180),
        Track(title='Track 2', artist='Artist 1', genre='Rock', duration=240),
        Track(title='Track 3', artist='Artist 2', genre='Pop', duration=200)
    ]
    
    with app.app_context():
        for track in tracks:
            db.session.add(track)
        db.session.commit()
    
    response = client.get('/api/stats')
    assert response.status_code == 200
    assert response.json['favorite_artist'] == 'Artist 1'
    assert 'Rock' in response.json['top_genres']
    assert response.json['total_duration'] == 620  # 180 + 240 + 200 