import sys
from PyQt5.QtWidgets import QApplication
from .view import MainWindow
from .controller import ClientController

def main():
    app = QApplication(sys.argv)
    
    # Создаем контроллер и окно
    controller = ClientController()
    window = MainWindow()
    
    # Обновляем данные при запуске
    tracks = controller.get_tracks()
    window.update_tracks(tracks)
    
    # Получаем и обновляем статистику
    stats = controller.get_stats()
    window.update_stats(stats)
    
    # Показываем окно
    window.show()
    
    # Запускаем приложение
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 