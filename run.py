from app import create_app, db
from app.models import User, Booking, Space, Category, Voucher
from datetime import datetime, timedelta, date


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
    if Space.query.count() > 0:
        return
    
    # 1. Kategori
    kategori_list = ['Co-Working', 'Meeting Room', 'Office Space', 'Event Space', 'Content Studio', 'Virtual Office']
    for nama in kategori_list:
        db.session.add(Category(nama_kategori=nama))
    db.session.commit()
    print("✅ Kategori berhasil dibuat.")
    
    # Ambil referensi kategori
    coworking_cat = Category.query.filter_by(nama_kategori='Co-Working').first()
    meeting_cat = Category.query.filter_by(nama_kategori='Meeting Room').first()
    office_cat = Category.query.filter_by(nama_kategori='Office Space').first()
    event_cat = Category.query.filter_by(nama_kategori='Event Space').first()
    studio_cat = Category.query.filter_by(nama_kategori='Content Studio').first()
    vo_cat = Category.query.filter_by(nama_kategori='Virtual Office').first()
    
    # URUTAN SANGAT PENTING — harus sesuai ID di MOCK_SPACES / index.html
    spaces = [
        # === MEETING ROOM (ID 1-3) ===
        Space(id=1, nama_ruangan='Meeting Room Small', deskripsi='Ruang rapat kecil untuk 4 orang. Dilengkapi AC, internet cepat, dan Smart TV 75 inch.', 
              harga_per_hari=150000, fasilitas='AC, High Speed Internet, 75" Smart TV', category_id=meeting_cat.id,
              gambar_url='https://placehold.co/800x500/0d6efd/ffffff?text=Meeting+Room+Small',
              durasi_default=1, durasi_satuan='Jam', durasi_tipe='flexible'),
        Space(id=2, nama_ruangan='Meeting Room Medium', deskripsi='Ruang rapat medium untuk 6 orang. Fasilitas lengkap dengan AC, internet cepat, dan Smart TV.',
              harga_per_hari=200000, fasilitas='AC, High Speed Internet, 75" Smart TV', category_id=meeting_cat.id,
              gambar_url='https://placehold.co/800x500/0d6efd/ffffff?text=Meeting+Room+Medium',
              durasi_default=1, durasi_satuan='Jam', durasi_tipe='flexible'),
        Space(id=3, nama_ruangan='Meeting Room Large', deskripsi='Ruang rapat besar untuk 15 orang. Cocok untuk presentasi atau diskusi tim besar.',
              harga_per_hari=300000, fasilitas='AC, High Speed Internet, 75" Smart TV', category_id=meeting_cat.id,
              gambar_url='https://placehold.co/800x500/0d6efd/ffffff?text=Meeting+Room+Large',
              durasi_default=1, durasi_satuan='Jam', durasi_tipe='flexible'),
        
        # === OFFICE SPACE (ID 4-6) ===
        Space(id=4, nama_ruangan='Office Space Small', deskripsi='Office space kecil untuk 3 orang. Furnished dan siap pakai.',
              harga_per_hari=5500000, fasilitas='Furnished, AC, Electricity, High Speed Internet, Electric Doorlock', category_id=office_cat.id,
              gambar_url='https://placehold.co/800x500/198754/ffffff?text=Office+Space+Small',
              durasi_default=1, durasi_satuan='Bulan', durasi_tipe='fixed'),
        Space(id=5, nama_ruangan='Office Space Medium', deskripsi='Office space medium untuk 5 orang. Cocok untuk tim startup.',
              harga_per_hari=6500000, fasilitas='Furnished, AC, Electricity, High Speed Internet, Electric Doorlock', category_id=office_cat.id,
              gambar_url='https://placehold.co/800x500/198754/ffffff?text=Office+Space+Medium',
              durasi_default=1, durasi_satuan='Bulan', durasi_tipe='fixed'),
        Space(id=6, nama_ruangan='Office Space Large', deskripsi='Office space besar untuk 10 orang. Ideal untuk tim yang sedang berkembang.',
              harga_per_hari=8500000, fasilitas='Furnished, AC, Electricity, High Speed Internet, Electric Doorlock', category_id=office_cat.id,
              gambar_url='https://placehold.co/800x500/198754/ffffff?text=Office+Space+Large',
              durasi_default=1, durasi_satuan='Bulan', durasi_tipe='fixed'),
        
        # === EVENT SPACE (ID 7-9) ===
        Space(id=7, nama_ruangan='Event Space Halfday', deskripsi='Sewa event space setengah hari (4 jam). Luas 88m², kapasitas hingga 100 orang.',
              harga_per_hari=4500000, fasilitas='Projector & Screen, Basic Soundsystem, Table & Chair, High Speed Internet, Catering Service', category_id=event_cat.id,
              gambar_url='https://placehold.co/800x500/dc3545/ffffff?text=Event+Space+Halfday',
              durasi_default=4, durasi_satuan='Jam', durasi_tipe='fixed'),
        Space(id=8, nama_ruangan='Event Space Fullday', deskripsi='Sewa event space sehari penuh (10 jam). Ideal untuk seminar dan workshop skala besar.',
              harga_per_hari=7500000, fasilitas='Projector & Screen, Basic Soundsystem, Table & Chair, High Speed Internet, Catering Service', category_id=event_cat.id,
              gambar_url='https://placehold.co/800x500/dc3545/ffffff?text=Event+Space+Fullday',
              durasi_default=10, durasi_satuan='Jam', durasi_tipe='fixed'),
        Space(id=9, nama_ruangan='Virtual Event', deskripsi='Paket virtual event dengan peralatan lengkap. Cocok untuk webinar atau siaran langsung skala besar.',
              harga_per_hari=7000000, fasilitas='Projector, Soundsystem, High Speed Internet', category_id=event_cat.id,
              gambar_url='https://placehold.co/800x500/dc3545/ffffff?text=Virtual+Event',
              durasi_default=10, durasi_satuan='Jam', durasi_tipe='fixed'),
        
        # === CONTENT STUDIO (ID 10-13) ===
        Space(id=10, nama_ruangan='IG Live & Podcast', deskripsi='Studio untuk siaran langsung Instagram atau rekaman podcast dengan kualitas audio profesional.',
              harga_per_hari=200000, fasilitas='Microphone, Lighting, High Speed Internet, AC', category_id=studio_cat.id,
              gambar_url='https://placehold.co/800x500/fd7e14/ffffff?text=IG+Live+Podcast',
              durasi_default=1, durasi_satuan='Jam', durasi_tipe='flexible'),
        Space(id=11, nama_ruangan='Webinar', deskripsi='Studio konten untuk webinar. Ruangan lebih luas dengan setup multi-kamera dan green screen opsional.',
              harga_per_hari=450000, fasilitas='Multi-Camera, Green Screen, Lighting, High Speed Internet, AC', category_id=studio_cat.id,
              gambar_url='https://placehold.co/800x500/fd7e14/ffffff?text=Webinar',
              durasi_default=3, durasi_satuan='Jam', durasi_tipe='fixed'),
        Space(id=12, nama_ruangan='Youtube Studio', deskripsi='Studio untuk produksi konten Youtube profesional dengan setup kamera sinematik.',
              harga_per_hari=1200000, fasilitas='Cinematic Camera, Studio Lighting, Sound System, High Speed Internet, AC', category_id=studio_cat.id,
              gambar_url='https://placehold.co/800x500/fd7e14/ffffff?text=Youtube+Studio',
              durasi_default=3, durasi_satuan='Jam', durasi_tipe='fixed'),
        Space(id=13, nama_ruangan='Photoshoot / Video Spot', deskripsi='Sewa area spesifik di CO&CO Hub untuk photoshoot atau pengambilan video.',
              harga_per_hari=600000, fasilitas='Pilihan Spot, Pencahayaan Alami, Area Luas', category_id=studio_cat.id,
              gambar_url='https://placehold.co/800x500/fd7e14/ffffff?text=Photoshoot+Spot',
              durasi_default=1, durasi_satuan='Jam', durasi_tipe='flexible'),
        
        # === VIRTUAL OFFICE (ID 14-15) ===
        Space(id=14, nama_ruangan='Virtual Office 1', deskripsi='Paket Virtual Office untuk alamat bisnis profesional. Cocok untuk startup atau perorangan.',
              harga_per_hari=3600000, fasilitas='Alamat Bisnis, Mail Handling, Resepsionis', category_id=vo_cat.id,
              gambar_url='https://placehold.co/800x500/6f42c1/ffffff?text=Virtual+Office+1',
              durasi_default=1, durasi_satuan='Tahun', durasi_tipe='fixed'),
        Space(id=15, nama_ruangan='Virtual Office 2', deskripsi='Paket Virtual Office premium dengan tambahan fasilitas Free Meeting Room.',
              harga_per_hari=4800000, fasilitas='Alamat Bisnis, Mail Handling, Resepsionis, Free Meeting Room', category_id=vo_cat.id,
              gambar_url='https://placehold.co/800x500/6f42c1/ffffff?text=Virtual+Office+2',
              durasi_default=1, durasi_satuan='Tahun', durasi_tipe='fixed'),
        
        # === CO-WORKING (ID 16-19) ===
        Space(id=16, nama_ruangan='Daily Pass', deskripsi='Akses coworking space selama sehari penuh (10 jam). Cocok untuk bekerja santai di luar rumah.',
              harga_per_hari=100000, fasilitas='WiFi, AC', category_id=coworking_cat.id,
              gambar_url='https://placehold.co/800x500/20c997/ffffff?text=Daily+Pass',
              durasi_default=10, durasi_satuan='Jam', durasi_tipe='fixed'),
        Space(id=17, nama_ruangan='3 Hours Pass', deskripsi='Akses coworking space selama 3 jam. Pas untuk mengerjakan tugas atau meeting singkat.',
              harga_per_hari=60000, fasilitas='WiFi, AC', category_id=coworking_cat.id,
              gambar_url='https://placehold.co/800x500/20c997/ffffff?text=3+Hours+Pass',
              durasi_default=3, durasi_satuan='Jam', durasi_tipe='fixed'),
        Space(id=18, nama_ruangan='Annual Pass', deskripsi='Paket hemat untuk 4 hari penggunaan coworking space dalam setahun. Bebas pilih hari.',
              harga_per_hari=300000, fasilitas='WiFi, AC', category_id=coworking_cat.id,
              gambar_url='https://placehold.co/800x500/20c997/ffffff?text=Annual+Pass',
              durasi_default=4, durasi_satuan='Hari', durasi_tipe='fixed'),
        Space(id=19, nama_ruangan='Resident Membership', deskripsi='Membership bulanan dengan akses tanpa batas ke coworking space.',
              harga_per_hari=1100000, fasilitas='WiFi, AC', category_id=coworking_cat.id,
              gambar_url='https://placehold.co/800x500/20c997/ffffff?text=Resident+Membership',
              durasi_default=1, durasi_satuan='Bulan', durasi_tipe='fixed'),
    ]
    for s in spaces:
        db.session.add(s)
    db.session.commit()
    print(f"✅ {len(spaces)} Space berhasil dibuat (ID 1-19).")
    
    # Booking dummy
    today = date.today()
    bookings = [
        Booking(kode_booking='BKG-2026-TEST01', nama_lengkap='Budi Santoso', email='budi@mail.com', no_whatsapp='081234567890',
                tanggal_mulai=today, durasi=1, total_harga=150000, status='pending', space_id=1),
        Booking(kode_booking='BKG-2026-TEST02', nama_lengkap='Siti Aminah', email='siti@mail.com', no_whatsapp='081298765432',
                tanggal_mulai=today + timedelta(days=2), durasi=10, total_harga=100000, status='sukses', space_id=16),
        Booking(kode_booking='BKG-2026-TEST03', nama_lengkap='Andi Wijaya', email='andi@mail.com', no_whatsapp='',
                tanggal_mulai=today - timedelta(days=5), durasi=6, total_harga=1200000, status='batal', space_id=2),
    ]
    for b in bookings:
        db.session.add(b)
    db.session.commit()
    print(f"✅ {len(bookings)} Booking dummy berhasil dibuat.")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_admin()
        seed_dummy_data()
        print("Database siap digunakan!")
    app.run(debug=True)