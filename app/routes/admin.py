from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import User, Booking, Space, Voucher, Category
from app.emails import kirim_email_status_update, generate_wifi_credentials

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# ==================== DASHBOARD ====================
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    total_bookings = Booking.query.count()
    total_spaces = Space.query.count()
    total_users = User.query.filter_by(role='user').count()
    total_vouchers = Voucher.query.count()
    recent_bookings = Booking.query.order_by(Booking.id.desc()).limit(5).all()
    stats = {
        'total_bookings': total_bookings,
        'total_spaces': total_spaces,
        'total_users': total_users,
        'total_vouchers': total_vouchers
    }
    return render_template('admin/dashboard.html', title='Dashboard', stats=stats, recent_bookings=recent_bookings)


# ==================== KELOLA PESANAN ====================
@admin_bp.route('/bookings')
@login_required
def bookings():
    search = request.args.get('search', '')
    if search:
        bookings_list = Booking.query.filter(
            (Booking.nama_lengkap.ilike(f'%{search}%')) | 
            (Booking.kode_booking.ilike(f'%{search}%'))
        ).order_by(Booking.id.desc()).all()
    else:
        bookings_list = Booking.query.order_by(Booking.id.desc()).all()
    return render_template('admin/bookings.html', title='Kelola Pesanan', bookings=bookings_list, search=search)


@admin_bp.route('/bookings/<int:booking_id>/status', methods=['POST'])
@login_required
def update_booking_status(booking_id):
    """Mengubah status pesanan + kirim email notifikasi."""
    booking = Booking.query.get_or_404(booking_id)
    new_status = request.form.get('status')
    
    if new_status not in ['pending', 'sukses', 'batal']:
        flash('Status tidak valid.', 'danger')
        return redirect(url_for('admin.bookings'))
    
    old_status = booking.status
    booking.status = new_status
    
    # KALAU BERUBAH KE SUKSES: Generate WiFi credentials
    if new_status == 'sukses' and old_status != 'sukses':
        # Kalau belum punya WiFi credentials, generate sekarang
        if not booking.wifi_username:
            wifi_user, wifi_pass = generate_wifi_credentials(booking.kode_booking)
            booking.wifi_username = wifi_user
            booking.wifi_password = wifi_pass
    
    db.session.commit()
    
    # Kirim email notifikasi kalau status berubah
    if old_status != new_status:
        kirim_email_status_update(booking)
        flash(f'Status pesanan #{booking.id} diubah ke {new_status.upper()} & email terkirim.', 'success')
    else:
        flash(f'Status pesanan #{booking.id} sudah {new_status.upper()}.', 'info')
    
    return redirect(url_for('admin.bookings'))


@admin_bp.route('/bookings/<int:booking_id>/delete', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash(f'Pesanan #{booking_id} berhasil dihapus.', 'success')
    return redirect(url_for('admin.bookings'))


# ==================== KELOLA RUANGAN ====================
@admin_bp.route('/spaces')
@login_required
def spaces():
    search = request.args.get('search', '')
    if search:
        spaces_list = Space.query.filter(Space.nama_ruangan.ilike(f'%{search}%')).order_by(Space.id.asc()).all()
    else:
        spaces_list = Space.query.order_by(Space.id.asc()).all()
    categories = Category.query.all()
    return render_template('admin/spaces.html', title='Kelola Ruangan', spaces=spaces_list, categories=categories, search=search)


@admin_bp.route('/spaces/create', methods=['POST'])
@login_required
def create_space():
    nama = request.form.get('nama_ruangan')
    deskripsi = request.form.get('deskripsi')
    harga = request.form.get('harga_per_hari')
    fasilitas = request.form.get('fasilitas')
    gambar_url = request.form.get('gambar_url')
    category_id = request.form.get('category_id')
    
    if not nama or not harga or not category_id:
        flash('Nama, harga, dan kategori wajib diisi!', 'danger')
        return redirect(url_for('admin.spaces'))
    
    new_space = Space(
        nama_ruangan=nama, deskripsi=deskripsi, harga_per_hari=int(harga),
        fasilitas=fasilitas,
        gambar_url=gambar_url if gambar_url else 'https://placehold.co/800x500/6c757d/ffffff?text=No+Image',
        category_id=int(category_id),
        durasi_default=1, durasi_satuan='Jam', durasi_tipe='flexible'
    )
    db.session.add(new_space)
    db.session.commit()
    flash(f'Ruangan "{nama}" berhasil ditambahkan!', 'success')
    return redirect(url_for('admin.spaces'))


@admin_bp.route('/spaces/<int:space_id>/edit', methods=['POST'])
@login_required
def edit_space(space_id):
    space = Space.query.get_or_404(space_id)
    space.nama_ruangan = request.form.get('nama_ruangan')
    space.deskripsi = request.form.get('deskripsi')
    space.harga_per_hari = int(request.form.get('harga_per_hari'))
    space.fasilitas = request.form.get('fasilitas')
    space.gambar_url = request.form.get('gambar_url')
    space.category_id = int(request.form.get('category_id'))
    db.session.commit()
    flash(f'Ruangan "{space.nama_ruangan}" berhasil diperbarui!', 'success')
    return redirect(url_for('admin.spaces'))


@admin_bp.route('/spaces/<int:space_id>/delete', methods=['POST'])
@login_required
def delete_space(space_id):
    space = Space.query.get_or_404(space_id)
    if space.bookings:
        flash(f'Tidak bisa menghapus "{space.nama_ruangan}" karena masih ada pesanan terkait.', 'danger')
        return redirect(url_for('admin.spaces'))
    nama = space.nama_ruangan
    db.session.delete(space)
    db.session.commit()
    flash(f'Ruangan "{nama}" berhasil dihapus.', 'success')
    return redirect(url_for('admin.spaces'))