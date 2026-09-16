import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'ini-kunci-rahasia-coworking-space-kamu'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'coworking.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Konfigurasi Upload File
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
    
    # ==========================================
    # KONFIGURASI EMAIL (GANTI BAGIAN INI!)
    # ==========================================
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    
    # ⚠️ GANTI DENGAN EMAIL & APP PASSWORD KAMU
    MAIL_USERNAME = 'pahruldrive@gmail.com'
    MAIL_PASSWORD = 'xpetzjbbswawqvak'  # 16 digit tanpa spasi
    MAIL_DEFAULT_SENDER = ('Booking CO&CO', 'pahruldrive@gmail.com')