# 🏢 CO&CO Hub - Coworking Space Booking System

Sistem pemesanan ruangan berbasis web untuk **CO&CO Hub** (Bandung). User bisa pesan ruangan tanpa login, admin mengelola via panel khusus.

---

## ✨ Fitur

**User (tanpa login):**
- Lihat daftar ruangan & harga (Co-Working, Meeting Room, Office, Event, Content Studio, Virtual Office)
- Detail ruangan + form booking pop-up
- Upload bukti transfer
- Dapat kode booking unik (contoh: `BKG-2026-A1B2C3`)

**Admin (wajib login):**
- Dashboard statistik
- CRUD Pesanan (ubah status: Pending/Sukses/Batal)
- CRUD Ruangan
- (Coming soon: Voucher, User, Integrasi Mikrotik)

---

## 🛠 Teknologi

| Komponen | Versi |
|---|---|
| Python | 3.13 |
| Flask | 2.3.3 |
| Flask-SQLAlchemy | 3.1.1 |
| Flask-Login | 0.6.3 |
| SQLAlchemy | 2.0.52 |
| Jinja2 | 3.1.6 |
| Bootstrap | 5.3.0 |
| Database | SQLite |

> ⚠️ **Tidak pakai Docker**. Jalankan langsung di Python.

---

## 📦 Prasyarat

Install dulu di PC kamu:
1. **Python 3.13+** → https://www.python.org/downloads/ (centang **Add Python to PATH**)
2. **Git** → https://git-scm.com/downloads
3. **VS Code** (opsional) → https://code.visualstudio.com/

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/PriosMilky/coworking_app.git
cd coworking_app
```

### 2. Buat Virtual Environment (WAJIB, di PC masing-masing)

**Windows CMD:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Windows Git Bash:**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> 💡 Setelah aktif, akan muncul `(.venv)` di terminal. Kalau tidak muncul, berarti belum aktif.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Cara Menjalankan

```bash
python run.py
```

Buka browser:
- **User:** http://127.0.0.1:5000/
- **Admin:** http://127.0.0.1:5000/admin/dashboard

---

## 🔑 Akun Admin Default

| Field | Value |
|---|---|
| Email | `admin@conco.id` |
| Password | `admin123` |

> ⚠️ Ganti password setelah login pertama!

---

## 📁 Struktur Proyek

```
coworking_app/
├── app/
│   ├── __init__.py          # Init Flask & extensions
│   ├── models.py            # Tabel database
│   ├── routes/              # Routing
│   │   ├── main.py          # User (Home, Detail)
│   │   ├── auth.py          # Login/Logout
│   │   ├── admin.py         # Panel admin
│   │   └── booking.py       # Proses booking
│   ├── templates/           # HTML (Jinja2)
│   │   ├── admin/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── room_detail.html
│   │   └── voucher.html
│   └── static/
│       └── uploads/         # Bukti transfer
├── config.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Cara Menggunakan

### User Side (Tanpa Login)

1. Buka http://127.0.0.1:5000/
2. Klik tab kategori (Meeting Room, Event Space, dll)
3. Klik **"Pilih Paket"** pada ruangan yang diinginkan
4. Klik tombol **"Book Now"** → form pop-up muncul
5. Isi: nama, email, tanggal, durasi, upload bukti transfer
6. Klik **"Kirim Pesanan"** → dapat kode booking

### Admin Side (Wajib Login)

1. Buka http://127.0.0.1:5000/admin/dashboard
2. Login: `admin@conco.id` / `admin123`
3. **Dashboard:** Lihat statistik
4. **Kelola Pesanan:** Ubah status pesanan (Pending/Sukses/Batal) atau hapus
5. **Kelola Ruangan:** Tambah/Edit/Hapus ruangan

---

## 🐛 Troubleshooting

**`TemplateNotFound: index.html`**
→ Pastikan semua file HTML ada di `app/templates/` dan sudah di-save (`Ctrl+S`).

**`ModuleNotFoundError: No module named 'flask'`**
→ Virtual environment belum aktif. Jalankan `source .venv/Scripts/activate` (Git Bash) atau `.venv\Scripts\activate` (CMD).

**Database error setelah update model**
→ Hapus file `coworking.db`, lalu `python run.py` ulang. Database akan dibuat ulang otomatis.

**Upload file gagal**
→ Pastikan folder `app/static/uploads/` sudah ada.

---

## 🗺️ Roadmap

- [x] Landing page & detail ruangan
- [x] Login admin
- [x] CRUD Pesanan & Ruangan
- [x] Form booking + upload bukti transfer
- [ ] Halaman cek status booking untuk user
- [ ] CRUD Voucher & User
- [ ] Integrasi Mikrotik RouterOS
- [ ] Notifikasi Email/WhatsApp
- [ ] Export laporan Excel/PDF

---