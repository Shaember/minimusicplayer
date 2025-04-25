from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Track:
    id: int
    title: str
    artist: str
    genre: str
    duration: int  # в секундах

@dataclass
class Playlist:
    id: int
    name: str
    tracks: List[Track]
    
    @property
    def duration(self) -> int:
        return sum(track.duration for track in self.tracks)

@dataclass
class UserStats:
    favorite_artist: Optional[str]
    top_genres: List[str]
    total_duration: int 