from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Таблица для связи многие-ко-многим между треками и плейлистами
track_playlist = Table(
    'track_playlist',
    Base.metadata,
    Column('track_id', Integer, ForeignKey('tracks.id')),
    Column('playlist_id', Integer, ForeignKey('playlists.id'))
)

class Track(Base):
    __tablename__ = 'tracks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    duration = Column(Integer, nullable=False)  # в секундах
    
    playlists = relationship("Playlist", secondary=track_playlist, back_populates="tracks")

class Playlist(Base):
    __tablename__ = 'playlists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    tracks = relationship("Track", secondary=track_playlist, back_populates="playlists") 