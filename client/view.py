from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QListWidget,
                            QLabel, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
from typing import List, Callable
from .model import Track, Playlist, UserStats

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniSpotify")
        self.setMinimumSize(800, 600)
        
        # Основной виджет
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Основной layout
        layout = QHBoxLayout()
        main_widget.setLayout(layout)
        
        # Левая панель (плейлисты)
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)
        
        self.playlist_list = QListWidget()
        left_layout.addWidget(QLabel("Плейлисты"))
        left_layout.addWidget(self.playlist_list)
        
        # Правая панель (треки)
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)
        
        self.track_list = QListWidget()
        right_layout.addWidget(QLabel("Треки"))
        right_layout.addWidget(self.track_list)
        
        # Добавляем панели в основной layout
        layout.addWidget(left_panel, 1)
        layout.addWidget(right_panel, 2)
        
        # Кнопки управления
        buttons_layout = QHBoxLayout()
        self.add_track_btn = QPushButton("Добавить трек")
        self.add_playlist_btn = QPushButton("Создать плейлист")
        buttons_layout.addWidget(self.add_track_btn)
        buttons_layout.addWidget(self.add_playlist_btn)
        right_layout.addLayout(buttons_layout)
        
        # Статистика
        stats_layout = QVBoxLayout()
        self.stats_label = QLabel()
        stats_layout.addWidget(QLabel("Статистика"))
        stats_layout.addWidget(self.stats_label)
        right_layout.addLayout(stats_layout)
    
    def update_tracks(self, tracks: List[Track]):
        self.track_list.clear()
        for track in tracks:
            self.track_list.addItem(f"{track.title} - {track.artist}")
    
    def update_playlists(self, playlists: List[Playlist]):
        self.playlist_list.clear()
        for playlist in playlists:
            self.playlist_list.addItem(playlist.name)
    
    def update_stats(self, stats: UserStats):
        stats_text = f"""
        Любимый исполнитель: {stats.favorite_artist or 'Нет данных'}
        Топ жанры: {', '.join(stats.top_genres)}
        Общая длительность: {stats.total_duration // 60} минут
        """
        self.stats_label.setText(stats_text)
    
    def show_error(self, message: str):
        QMessageBox.critical(self, "Ошибка", message)
    
    def show_info(self, message: str):
        QMessageBox.information(self, "Информация", message) 