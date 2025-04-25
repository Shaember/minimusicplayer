import requests
from typing import List
from .model import Track, Playlist, UserStats

class ClientController:
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url
    
    def get_tracks(self) -> List[Track]:
        response = requests.get(f"{self.base_url}/tracks")
        if response.status_code == 200:
            return [Track(**track) for track in response.json()]
        return []
    
    def add_track(self, title: str, artist: str, genre: str, duration: int) -> bool:
        data = {
            "title": title,
            "artist": artist,
            "genre": genre,
            "duration": duration
        }
        response = requests.post(f"{self.base_url}/track", json=data)
        return response.status_code == 201
    
    def get_stats(self) -> UserStats:
        response = requests.get(f"{self.base_url}/stats")
        if response.status_code == 200:
            return UserStats(**response.json())
        return UserStats(None, [], 0)
    
    def calculate_top_genres(self, tracks: List[Track]) -> List[str]:
        genre_count = {}
        for track in tracks:
            genre_count[track.genre] = genre_count.get(track.genre, 0) + 1
        return sorted(genre_count.keys(), key=lambda x: genre_count[x], reverse=True)[:3]
    
    def calculate_favorite_artist(self, tracks: List[Track]) -> str:
        artist_count = {}
        for track in tracks:
            artist_count[track.artist] = artist_count.get(track.artist, 0) + 1
        return max(artist_count.items(), key=lambda x: x[1])[0] if artist_count else None 