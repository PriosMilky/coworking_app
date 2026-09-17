import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'eD=7NS4W*$nQZHG3!zw2+m9f6&yUFbY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'coworking.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload File
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
    
    # Email (Gmail)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'pahruldrive@gmail.com'
    MAIL_PASSWORD = 'xpetzjbbswawqvak'
    MAIL_DEFAULT_SENDER = ('Booking CO&CO', 'pahruldrive@gmail.com')
    
    # Google Sheets Webhook
    GOOGLE_SHEET_WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbzgWJiNMXjIiwG0oSnXBPtxaRE2roNd_uDwmtNR4r5boj7tUuvdyxqZv8qtLjUYGfyEVA/exec'