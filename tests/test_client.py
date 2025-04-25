import pytest
from client.model import Track, Playlist, UserStats
from client.controller import ClientController

def test_track_creation():
    track = Track(
        id=1,
        title="Test Track",
        artist="Test Artist",
        genre="Rock",
        duration=180
    )
    assert track.title == "Test Track"
    assert track.artist == "Test Artist"
    assert track.genre == "Rock"
    assert track.duration == 180

def test_playlist_duration():
    tracks = [
        Track(id=1, title="Track 1", artist="Artist 1", genre="Rock", duration=180),
        Track(id=2, title="Track 2", artist="Artist 2", genre="Pop", duration=240)
    ]
    playlist = Playlist(id=1, name="Test Playlist", tracks=tracks)
    assert playlist.duration == 420  # 180 + 240

def test_controller_stats_calculation():
    controller = ClientController()
    tracks = [
        Track(id=1, title="Track 1", artist="Artist 1", genre="Rock", duration=180),
        Track(id=2, title="Track 2", artist="Artist 1", genre="Rock", duration=240),
        Track(id=3, title="Track 3", artist="Artist 2", genre="Pop", duration=200)
    ]
    
    top_genres = controller.calculate_top_genres(tracks)
    assert len(top_genres) == 2
    assert top_genres[0] == "Rock"
    
    favorite_artist = controller.calculate_favorite_artist(tracks)
    assert favorite_artist == "Artist 1" 