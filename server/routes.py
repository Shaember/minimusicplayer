from flask import Blueprint, jsonify, request
from sqlalchemy import func
from .models import db, Track, Playlist

api = Blueprint('api', __name__)

@api.route('/tracks', methods=['GET'])
def get_tracks():
    tracks = Track.query.all()
    return jsonify([{
        'id': track.id,
        'title': track.title,
        'artist': track.artist,
        'genre': track.genre,
        'duration': track.duration
    } for track in tracks])

@api.route('/track', methods=['POST'])
def add_track():
    data = request.get_json()
    
    track = Track(
        title=data['title'],
        artist=data['artist'],
        genre=data['genre'],
        duration=data['duration']
    )
    
    db.session.add(track)
    db.session.commit()
    
    return jsonify({
        'id': track.id,
        'title': track.title,
        'artist': track.artist,
        'genre': track.genre,
        'duration': track.duration
    }), 201

@api.route('/stats', methods=['GET'])
def get_stats():
    # Получаем любимого исполнителя
    favorite_artist = db.session.query(
        Track.artist,
        func.count(Track.id).label('count')
    ).group_by(Track.artist).order_by(func.count(Track.id).desc()).first()
    
    # Получаем топ жанров
    top_genres = db.session.query(
        Track.genre,
        func.count(Track.id).label('count')
    ).group_by(Track.genre).order_by(func.count(Track.id).desc()).limit(3).all()
    
    # Получаем общую длительность
    total_duration = db.session.query(func.sum(Track.duration)).scalar() or 0
    
    return jsonify({
        'favorite_artist': favorite_artist[0] if favorite_artist else None,
        'top_genres': [genre[0] for genre in top_genres],
        'total_duration': total_duration
    }) 