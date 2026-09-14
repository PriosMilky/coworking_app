import os
import random
import string
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models import Booking, Space

booking_bp = Blueprint('booking', __name__, url_prefix='/booking')


def allowed_file(filename):
    """Cek apakah ekstensi file diizinkan."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def generate_kode_booking():
    """Generate kode booking unik: BKG-XXXXXX"""
    tahun = datetime.now().year
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"BKG-{tahun}-{random_str}"


@booking_bp.route('/create', methods=['POST'])
def create():
    """Memproses form pemesanan dari user."""
    
    # 1. Ambil data dari form
    space_id = request.form.get('space_id')
    nama_lengkap = request.form.get('nama_lengkap')
    email = request.form.get('email')
    no_whatsapp = request.form.get('no_whatsapp', '')
    tanggal_mulai_str = request.form.get('tanggal_mulai')
    durasi = request.form.get('durasi')
    
    # 2. Validasi
    if not all([space_id, nama_lengkap, email, tanggal_mulai_str, durasi]):
        flash('Semua field wajib diisi!', 'danger')
        return redirect(url_for('main.room_detail', room_id=space_id))
    
    space = Space.query.get(space_id)
    if not space:
        flash('Ruangan tidak ditemukan.', 'danger')
        return redirect(url_for('main.index'))
    
    # 3. Proses Upload Bukti Pembayaran
    file = request.files.get('bukti_pembayaran')
    filename = None
    
    if file and file.filename != '':
        if not allowed_file(file.filename):
            flash('Format file harus JPG, PNG, atau PDF!', 'danger')
            return redirect(url_for('main.room_detail', room_id=space_id))
        
        # Buat nama file unik: timestamp_namafile
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        original_name = secure_filename(file.filename)
        filename = f"{timestamp}_{original_name}"
        
        # Pastikan folder upload ada
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        
        # Simpan file
        file.save(os.path.join(upload_folder, filename))
    
    # 4. Hitung total harga & tanggal selesai
    tanggal_mulai = datetime.strptime(tanggal_mulai_str, '%Y-%m-%d').date()
    durasi_int = int(durasi)
    
    # Asumsi: durasi dalam jam, harga per hari (8 jam = 1 hari harga)
    # Untuk Co-Working: Rp 100.000/day = 8 jam. Jadi per jam Rp 12.500.
    # Untuk Meeting Room: Rp 150.000/hour. 
    # Kita sederhanakan: total_harga = harga_per_hari * durasi (nanti bisa diperbaiki)
    total_harga = space.harga_per_hari * durasi_int
    
    # 5. Buat booking baru
    booking = Booking(
        kode_booking=generate_kode_booking(),
        nama_lengkap=nama_lengkap,
        email=email,
        no_whatsapp=no_whatsapp,
        tanggal_mulai=tanggal_mulai,
        durasi=durasi_int,
        total_harga=total_harga,
        bukti_pembayaran=filename,
        status='pending',
        space_id=space.id
    )
    
    db.session.add(booking)
    db.session.commit()
    
    # 6. Redirect ke halaman voucher dengan kode booking
    return redirect(url_for('booking.success', kode=booking.kode_booking))


@booking_bp.route('/success/<kode>')
def success(kode):
    """Halaman sukses dengan voucher/token booking."""
    booking = Booking.query.filter_by(kode_booking=kode).first_or_404()
    return render_template('voucher.html', title='Booking Berhasil', booking=booking)