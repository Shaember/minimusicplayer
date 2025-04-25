from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .routes import api

# Инициализация Flask приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db = SQLAlchemy(app)

# Регистрация Blueprint
app.register_blueprint(api, url_prefix='/api')

# Создание таблиц
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    ) 