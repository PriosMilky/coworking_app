from app import create_app, db
from app.models import User, Booking, Space, Category, Voucher
from datetime import datetime, timedelta

app = create_app()

def seed_admin():
    admin = User.query.filter_by(email='admin@conco.id').first()
    if not admin:
        admin = User(nama_lengkap='Administrator', email='admin@conco.id', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("✅ Akun admin berhasil dibuat!")

def seed_dummy_data():
    """Membuat data dummy untuk uji coba CRUD."""
    # Cek apakah sudah ada data
    if Space.query.count() > 0:
        return
    
    # 1. Buat Kategori
    kategori_list = ['Co-Working', 'Meeting Room', 'Office Space', 'Event Space', 'Content Studio', 'Virtual Office']
    for nama in kategori_list:
        db.session.add(Category(nama_kategori=nama))
    db.session.commit()
    print("✅ Kategori berhasil dibuat.")
    
    # 2. Buat beberapa Space
    coworking_cat = Category.query.filter_by(nama_kategori='Co-Working').first()
    meeting_cat = Category.query.filter_by(nama_kategori='Meeting Room').first()
    
    spaces = [
        Space(nama_ruangan='Daily Pass', deskripsi='Akses sehari penuh', harga_per_hari=100000, fasilitas='WiFi, AC', category_id=coworking_cat.id),
        Space(nama_ruangan='Meeting Room Small', deskripsi='Ruang meeting 4 orang', harga_per_hari=150000, fasilitas='AC, TV, WiFi', category_id=meeting_cat.id),
        Space(nama_ruangan='Meeting Room Medium', deskripsi='Ruang meeting 6 orang', harga_per_hari=200000, fasilitas='AC, TV, WiFi', category_id=meeting_cat.id),
    ]
    for s in spaces:
        db.session.add(s)
    db.session.commit()
    print("✅ Space berhasil dibuat.")
    
    # 3. Buat User Dummy
    user1 = User(nama_lengkap='Budi Santoso', email='budi@mail.com', role='user')
    user1.set_password('password')
    user2 = User(nama_lengkap='Siti Aminah', email='siti@mail.com', role='user')
    user2.set_password('password')
    db.session.add_all([user1, user2])
    db.session.commit()
    
    # 4. Buat Booking Dummy
    today = datetime.utcnow()
    bookings = [
        Booking(tanggal_mulai=today, tanggal_selesai=today + timedelta(days=1), total_harga=100000, status='pending', user_id=user1.id, space_id=1),
        Booking(tanggal_mulai=today + timedelta(days=2), tanggal_selesai=today + timedelta(days=3), total_harga=200000, status='sukses', user_id=user2.id, space_id=2),
        Booking(tanggal_mulai=today - timedelta(days=5), tanggal_selesai=today - timedelta(days=4), total_harga=150000, status='batal', user_id=user1.id, space_id=3),
    ]
    for b in bookings:
        db.session.add(b)
    db.session.commit()
    print("✅ Data booking dummy berhasil dibuat.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_admin()
        seed_dummy_data()
        print("Database siap digunakan!")
    app.run(debug=True)