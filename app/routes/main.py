from flask import Blueprint, render_template, abort, request, flash
from app.models import Space, Category, Booking

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    categories = Category.query.all()
    
    spaces_by_category = {}
    for cat in categories:
        spaces_by_category[cat.nama_kategori] = Space.query.filter_by(category_id=cat.id).order_by(Space.id).all()
    
    return render_template(
        'index.html',
        title='Home',
        categories=categories,
        spaces_by_category=spaces_by_category
    )


@main_bp.route('/room/<int:room_id>')
def room_detail(room_id):
    space = Space.query.get(room_id)
    if space is None:
        abort(404)
    
    room = {
        'id': space.id,
        'nama': space.nama_ruangan,
        'kategori': space.category.nama_kategori,
        'kapasitas': '-',
        'harga': f'Rp {space.harga_per_hari:,}'.replace(',', '.'),
        'satuan': f"/ {space.durasi_satuan}",
        'deskripsi': space.deskripsi,
        'fasilitas': [f.strip() for f in space.fasilitas.split(',')] if space.fasilitas else [],
        'gambar_utama': space.gambar_url or 'https://placehold.co/800x500/6c757d/ffffff?text=No+Image',
        'gambar_thumb': [
            'https://placehold.co/150x100/6c757d/ffffff?text=Foto+1',
            'https://placehold.co/150x100/6c757d/ffffff?text=Foto+2',
            'https://placehold.co/150x100/6c757d/ffffff?text=Foto+3'
        ],
        'durasi_default': space.durasi_default,
        'durasi_satuan': space.durasi_satuan,
        'durasi_tipe': space.durasi_tipe,
    }
    
    return render_template('room_detail.html', title=space.nama_ruangan, room=room)

@main_bp.route('/cek-status', methods=['GET', 'POST'])
def cek_status():
    """Halaman untuk user cek status booking berdasarkan kode."""
    booking = None
    kode = None
    
    # Kalau ada kode di URL (dari email), langsung tampilkan
    kode = request.args.get('kode')
    
    if kode:
        booking = Booking.query.filter_by(kode_booking=kode).first()
    
    # Kalau user submit form manual
    if request.method == 'POST':
        kode = request.form.get('kode_booking', '').strip().upper()
        if kode:
            booking = Booking.query.filter_by(kode_booking=kode).first()
            if not booking:
                flash(f'Kode booking "{kode}" tidak ditemukan.', 'danger')
    
    return render_template('cek_status.html', title='Cek Status Booking', booking=booking, kode=kode)