from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='admin') # 'admin' atau 'user'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.nama_lengkap}', '{self.email}')"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_kategori = db.Column(db.String(50), nullable=False)
    spaces = db.relationship('Space', backref='category', lazy=True)

class Space(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_ruangan = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=True)
    harga_per_hari = db.Column(db.Integer, nullable=False)
    fasilitas = db.Column(db.Text, nullable=True)
    gambar_url = db.Column(db.String(255), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    # --- FIELD BARU UNTUK DURASI ---
    durasi_default = db.Column(db.Integer, nullable=True, default=1)
    durasi_satuan = db.Column(db.String(20), default='Jam')       # Jam, Hari, Bulan, Tahun
    durasi_tipe = db.Column(db.String(20), default='flexible')    # 'fixed' atau 'flexible'
    
    bookings = db.relationship('Booking', backref='space', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kode_booking = db.Column(db.String(20), unique=True, nullable=False)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    no_whatsapp = db.Column(db.String(20), nullable=True)
    tanggal_mulai = db.Column(db.Date, nullable=False)
    durasi = db.Column(db.Integer, nullable=False)
    total_harga = db.Column(db.Integer, nullable=False)
    bukti_pembayaran = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # --- FIELD BARU UNTUK WIFI VOUCHER ---
    wifi_username = db.Column(db.String(50), nullable=True)
    wifi_password = db.Column(db.String(50), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    space_id = db.Column(db.Integer, db.ForeignKey('space.id'), nullable=False)

class Voucher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kode_voucher = db.Column(db.String(50), unique=True, nullable=False)
    is_used = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)