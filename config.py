import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'ini-kunci-rahasia-coworking-space-kamu'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'coworking.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Konfigurasi Upload File
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # Maksimal 5 MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}