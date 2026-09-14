from flask import Blueprint, render_template, abort

main_bp = Blueprint('main', __name__)

MOCK_SPACES = {
    # --- MEETING ROOMS (1-3) ---
    1: {
        'id': 1, 'nama': 'Meeting Room Small', 'kategori': 'Meeting Room',
        'kapasitas': '4 Person', 'harga': 'Rp 150.000', 'satuan': '/ Hour',
        'deskripsi': 'Ruang rapat kecil yang nyaman, cocok untuk meeting tim berisi 4 orang. Dilengkapi dengan AC, High Speed Internet, dan Smart TV 75 inch.',
        'fasilitas': ['AC', 'High Speed Internet', '75" Smart TV'],
        'gambar_utama': 'https://placehold.co/800x500/0d6efd/ffffff?text=Meeting+Room+Small',
        'gambar_thumb': ['https://placehold.co/150x100/0d6efd/ffffff?text=Foto+1', 'https://placehold.co/150x100/0d6efd/ffffff?text=Foto+2']
    },
    2: {
        'id': 2, 'nama': 'Meeting Room Medium', 'kategori': 'Meeting Room',
        'kapasitas': '6 Person', 'harga': 'Rp 200.000', 'satuan': '/ Hour',
        'deskripsi': 'Ruang rapat medium untuk 6 orang. Fasilitas lengkap dengan AC, High Speed Internet, dan Smart TV 75 inch.',
        'fasilitas': ['AC', 'High Speed Internet', '75" Smart TV'],
        'gambar_utama': 'https://placehold.co/800x500/0d6efd/ffffff?text=Meeting+Room+Medium',
        'gambar_thumb': ['https://placehold.co/150x100/0d6efd/ffffff?text=Foto+1', 'https://placehold.co/150x100/0d6efd/ffffff?text=Foto+2']
    },
    3: {
        'id': 3, 'nama': 'Meeting Room Large', 'kategori': 'Meeting Room',
        'kapasitas': '15 Person', 'harga': 'Rp 300.000', 'satuan': '/ Hour',
        'deskripsi': 'Ruang rapat besar untuk 15 orang. Sangat cocok untuk presentasi atau diskusi tim yang lebih besar.',
        'fasilitas': ['AC', 'High Speed Internet', '75" Smart TV'],
        'gambar_utama': 'https://placehold.co/800x500/0d6efd/ffffff?text=Meeting+Room+Large',
        'gambar_thumb': ['https://placehold.co/150x100/0d6efd/ffffff?text=Foto+1', 'https://placehold.co/150x100/0d6efd/ffffff?text=Foto+2']
    },

    # --- OFFICE SPACES (4-6) ---
    4: {
        'id': 4, 'nama': 'Office Space Small', 'kategori': 'Office Space',
        'kapasitas': '3 Person', 'harga': 'Rp 5.500.000', 'satuan': '/ Month',
        'deskripsi': 'Office space kecil untuk 3 orang. Fasilitas lengkap dengan Furnished, AC, Electricity, High Speed Internet, dan Electric Doorlock.',
        'fasilitas': ['Furnished', 'AC', 'Electricity', 'High Speed Internet', 'Electric Doorlock'],
        'gambar_utama': 'https://placehold.co/800x500/198754/ffffff?text=Office+Space+Small',
        'gambar_thumb': ['https://placehold.co/150x100/198754/ffffff?text=Foto+1', 'https://placehold.co/150x100/198754/ffffff?text=Foto+2']
    },
    5: {
        'id': 5, 'nama': 'Office Space Medium', 'kategori': 'Office Space',
        'kapasitas': '5 Person', 'harga': 'Rp 6.500.000', 'satuan': '/ Month',
        'deskripsi': 'Office space medium untuk 5 orang. Fasilitas lengkap dengan Furnished, AC, Electricity, High Speed Internet, dan Electric Doorlock.',
        'fasilitas': ['Furnished', 'AC', 'Electricity', 'High Speed Internet', 'Electric Doorlock'],
        'gambar_utama': 'https://placehold.co/800x500/198754/ffffff?text=Office+Space+Medium',
        'gambar_thumb': ['https://placehold.co/150x100/198754/ffffff?text=Foto+1', 'https://placehold.co/150x100/198754/ffffff?text=Foto+2']
    },
    6: {
        'id': 6, 'nama': 'Office Space Large', 'kategori': 'Office Space',
        'kapasitas': '10 Person', 'harga': 'Rp 8.500.000', 'satuan': '/ Month',
        'deskripsi': 'Office space besar untuk 10 orang. Fasilitas lengkap dengan Furnished, AC, Electricity, High Speed Internet, dan Electric Doorlock.',
        'fasilitas': ['Furnished', 'AC', 'Electricity', 'High Speed Internet', 'Electric Doorlock'],
        'gambar_utama': 'https://placehold.co/800x500/198754/ffffff?text=Office+Space+Large',
        'gambar_thumb': ['https://placehold.co/150x100/198754/ffffff?text=Foto+1', 'https://placehold.co/150x100/198754/ffffff?text=Foto+2']
    },

    # --- EVENT SPACES (7-9) ---
    7: {
        'id': 7, 'nama': 'Event Space - Halfday', 'kategori': 'Event Space',
        'kapasitas': 'Up to 100 Person', 'harga': 'Rp 4.500.000', 'satuan': '/ 4 Hours',
        'deskripsi': 'Sewa event space setengah hari (4 jam). Luas ruangan 88m², kapasitas hingga 100 orang. Cocok untuk seminar, workshop, atau gathering.',
        'fasilitas': ['Projector & Screen', 'Basic Soundsystem', 'Table & Chair', 'High Speed Internet', 'Catering Service'],
        'gambar_utama': 'https://placehold.co/800x500/dc3545/ffffff?text=Event+Space+Halfday',
        'gambar_thumb': ['https://placehold.co/150x100/dc3545/ffffff?text=Foto+1', 'https://placehold.co/150x100/dc3545/ffffff?text=Foto+2']
    },
    8: {
        'id': 8, 'nama': 'Event Space - Fullday', 'kategori': 'Event Space',
        'kapasitas': 'Up to 100 Person', 'harga': 'Rp 7.500.000', 'satuan': '/ 8 Hours',
        'deskripsi': 'Sewa event space sehari penuh (8 jam). Luas ruangan 88m², kapasitas hingga 100 orang. Dilengkapi Projector, Soundsystem, dan Catering service.',
        'fasilitas': ['Projector & Screen', 'Basic Soundsystem', 'Table & Chair', 'High Speed Internet', 'Catering Service'],
        'gambar_utama': 'https://placehold.co/800x500/dc3545/ffffff?text=Event+Space+Fullday',
        'gambar_thumb': ['https://placehold.co/150x100/dc3545/ffffff?text=Foto+1', 'https://placehold.co/150x100/dc3545/ffffff?text=Foto+2']
    },
    9: {
        'id': 9, 'nama': 'Virtual Event', 'kategori': 'Event Space',
        'kapasitas': 'Unlimited', 'harga': 'Rp 7.000.000', 'satuan': '',
        'deskripsi': 'Paket virtual event dengan peralatan lengkap. Cocok untuk webinar atau siaran langsung skala besar.',
        'fasilitas': ['Projector & Screen', 'Basic Soundsystem', 'High Speed Internet'],
        'gambar_utama': 'https://placehold.co/800x500/dc3545/ffffff?text=Virtual+Event',
        'gambar_thumb': ['https://placehold.co/150x100/dc3545/ffffff?text=Foto+1', 'https://placehold.co/150x100/dc3545/ffffff?text=Foto+2']
    },

    # --- CONTENT STUDIO (10, 20, 11, 12, 13) ---
    10: {
        'id': 10, 'nama': 'IG Live', 'kategori': 'Content Studio',
        'kapasitas': '2 Person', 'harga': 'Rp 200.000', 'satuan': '/ Hour',
        'deskripsi': 'Studio untuk siaran langsung Instagram. Dilengkapi microphone dan pencahayaan standar studio.',
        'fasilitas': ['WiFi', 'AC', 'Microphone', 'Lighting'],
        'gambar_utama': 'https://placehold.co/800x500/fd7e14/ffffff?text=IG+Live',
        'gambar_thumb': ['https://placehold.co/150x100/fd7e14/ffffff?text=Foto+1', 'https://placehold.co/150x100/fd7e14/ffffff?text=Foto+2']
    },
    20: {
        'id': 20, 'nama': 'Podcast', 'kategori': 'Content Studio',
        'kapasitas': '4 Person', 'harga': 'Rp 450.000', 'satuan': '/ 3 Hours',
        'deskripsi': 'Studio untuk rekaman podcast dengan kualitas audio profesional. Cocok untuk diskusi santai maupun formal.',
        'fasilitas': ['WiFi', 'AC', 'Microphone', 'Lighting'],
        'gambar_utama': 'https://placehold.co/800x500/fd7e14/ffffff?text=Podcast',
        'gambar_thumb': ['https://placehold.co/150x100/fd7e14/ffffff?text=Foto+1', 'https://placehold.co/150x100/fd7e14/ffffff?text=Foto+2']
    },
    11: {
        'id': 11, 'nama': 'Webinar', 'kategori': 'Content Studio',
        'kapasitas': '10 Person', 'harga': 'Rp 450.000', 'satuan': '/ 3 Hours',
        'deskripsi': 'Studio konten untuk webinar. Ruangan lebih luas dengan setup multi-kamera dan green screen opsional.',
        'fasilitas': ['WiFi', 'AC', 'Multi-Camera', 'Green Screen', 'Lighting'],
        'gambar_utama': 'https://placehold.co/800x500/fd7e14/ffffff?text=Webinar',
        'gambar_thumb': ['https://placehold.co/150x100/fd7e14/ffffff?text=Foto+1', 'https://placehold.co/150x100/fd7e14/ffffff?text=Foto+2']
    },
    12: {
        'id': 12, 'nama': 'Youtube', 'kategori': 'Content Studio',
        'kapasitas': '6 Person', 'harga': 'Rp 1.200.000', 'satuan': '/ 3 Hours',
        'deskripsi': 'Studio untuk produksi konten Youtube profesional. Setup kamera sinematik, lighting, dan sound system berkualitas tinggi.',
        'fasilitas': ['WiFi', 'AC', 'Cinematic Camera', 'Studio Lighting', 'Sound System'],
        'gambar_utama': 'https://placehold.co/800x500/fd7e14/ffffff?text=Youtube',
        'gambar_thumb': ['https://placehold.co/150x100/fd7e14/ffffff?text=Foto+1', 'https://placehold.co/150x100/fd7e14/ffffff?text=Foto+2']
    },
    13: {
        'id': 13, 'nama': 'Photoshoot / Video Spot', 'kategori': 'Content Studio',
        'kapasitas': 'Sesuai Kebutuhan', 'harga': 'Rp 600.000', 'satuan': '/ Hour per Spot',
        'deskripsi': 'Sewa area spesifik di CO&CO Hub untuk keperluan photoshoot atau pengambilan video.',
        'fasilitas': ['WiFi', 'AC', 'Pilihan Spot', 'Pencahayaan Alami'],
        'gambar_utama': 'https://placehold.co/800x500/fd7e14/ffffff?text=Photoshoot+Spot',
        'gambar_thumb': ['https://placehold.co/150x100/fd7e14/ffffff?text=Foto+1', 'https://placehold.co/150x100/fd7e14/ffffff?text=Foto+2']
    },

    # --- VIRTUAL OFFICE (14-15) ---
    14: {
        'id': 14, 'nama': 'Virtual Office 1', 'kategori': 'Virtual Office',
        'kapasitas': 'Startup / Perorangan', 'harga': 'Rp 3.600.000', 'satuan': '/ Year',
        'deskripsi': 'Paket Virtual Office untuk alamat bisnis profesional. Cocok untuk startup atau perorangan yang membutuhkan alamat usaha resmi.',
        'fasilitas': ['Alamat Bisnis', 'Mail Handling', 'Resepsionis'],
        'gambar_utama': 'https://placehold.co/800x500/6f42c1/ffffff?text=Virtual+Office+1',
        'gambar_thumb': ['https://placehold.co/150x100/6f42c1/ffffff?text=Foto+1', 'https://placehold.co/150x100/6f42c1/ffffff?text=Foto+2']
    },
    15: {
        'id': 15, 'nama': 'Virtual Office 2', 'kategori': 'Virtual Office',
        'kapasitas': 'Bisnis Skala Menengah', 'harga': 'Rp 4.800.000', 'satuan': '/ Year',
        'deskripsi': 'Paket Virtual Office premium dengan tambahan fasilitas Free Meeting Room. Cocok untuk bisnis skala menengah.',
        'fasilitas': ['Alamat Bisnis', 'Mail Handling', 'Resepsionis', 'Free Meeting Room'],
        'gambar_utama': 'https://placehold.co/800x500/6f42c1/ffffff?text=Virtual+Office+2',
        'gambar_thumb': ['https://placehold.co/150x100/6f42c1/ffffff?text=Foto+1', 'https://placehold.co/150x100/6f42c1/ffffff?text=Foto+2']
    },

    # --- CO-WORKING (16-19) ---
    16: {
        'id': 16, 'nama': 'Daily Pass', 'kategori': 'Co-Working',
        'kapasitas': '1 Person', 'harga': 'Rp 100.000', 'satuan': '/ Day (8 Hours)',
        'deskripsi': 'Akses coworking space selama sehari penuh (8 jam). Cocok untuk kamu yang ingin bekerja santai di luar rumah.',
        'fasilitas': ['WiFi', 'AC'],
        'gambar_utama': 'https://placehold.co/800x500/20c997/ffffff?text=Daily+Pass',
        'gambar_thumb': ['https://placehold.co/150x100/20c997/ffffff?text=Foto+1', 'https://placehold.co/150x100/20c997/ffffff?text=Foto+2']
    },
    17: {
        'id': 17, 'nama': '3 Hours Pass', 'kategori': 'Co-Working',
        'kapasitas': '1 Person', 'harga': 'Rp 60.000', 'satuan': '/ 3 Hours',
        'deskripsi': 'Akses coworking space selama 3 jam. Pilihan pas untuk mengerjakan tugas atau meeting singkat.',
        'fasilitas': ['WiFi', 'AC'],
        'gambar_utama': 'https://placehold.co/800x500/20c997/ffffff?text=3+Hours+Pass',
        'gambar_thumb': ['https://placehold.co/150x100/20c997/ffffff?text=Foto+1', 'https://placehold.co/150x100/20c997/ffffff?text=Foto+2']
    },
    18: {
        'id': 18, 'nama': 'Annual Pass', 'kategori': 'Co-Working',
        'kapasitas': '1 Person', 'harga': 'Rp 300.000', 'satuan': '/ 4 Days',
        'deskripsi': 'Paket hemat untuk 4 hari penggunaan coworking space dalam setahun. Bebas pilih hari kapan saja.',
        'fasilitas': ['WiFi', 'AC'],
        'gambar_utama': 'https://placehold.co/800x500/20c997/ffffff?text=Annual+Pass',
        'gambar_thumb': ['https://placehold.co/150x100/20c997/ffffff?text=Foto+1', 'https://placehold.co/150x100/20c997/ffffff?text=Foto+2']
    },
    19: {
        'id': 19, 'nama': 'Resident Membership', 'kategori': 'Co-Working',
        'kapasitas': '1 Person', 'harga': 'Rp 1.100.000', 'satuan': '/ Month',
        'deskripsi': 'Membership bulanan dengan akses tanpa batas ke coworking space. Fasilitas WiFi dan AC sudah termasuk.',
        'fasilitas': ['WiFi', 'AC'],
        'gambar_utama': 'https://placehold.co/800x500/20c997/ffffff?text=Resident+Membership',
        'gambar_thumb': ['https://placehold.co/150x100/20c997/ffffff?text=Foto+1', 'https://placehold.co/150x100/20c997/ffffff?text=Foto+2']
    }
}

@main_bp.route('/')
def index():
    return render_template('index.html', title='Home')

@main_bp.route('/room/<int:room_id>')
def room_detail(room_id):
    room = MOCK_SPACES.get(room_id)
    if room is None:
        abort(404)
    return render_template('room_detail.html', title=room['nama'], room=room)