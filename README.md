## 🏢 CO&CO Hub - Coworking Space Booking System

Sistem pemesanan ruangan berbasis web untuk CO&CO Hub (Bandung).

## 🚀 Cara Menjalankan Cepat

- 1. Clone atau Download Repository:

git clone https://github.com/PriosMilky/coworking_app.git cd coworking_app

- 2. Buat & Aktifkan Virtual Environment:

- Windows (CMD):

python -m venv .venv .venv\Scripts\activate

- Windows (Git Bash):

python -m venv .venv source .venv/Scripts/activate

- Linux/Mac:

python3 -m venv .venv source .venv/bin/activate

- 3. Install Dependencies & Jalankan Aplikasi:

pip install -r requirements.txt

python run.py

- 4. Buka di Browser:

- User: http://127.0.0.1:5000/ [URL 🔗](http://127.0.0.1:5000/?utm_source=gemini)

Admin: http://127.0.0.1:5000/admin/dashboard (Login: admin@conco.id / admin123) [URL 🔗](http://127.0.0.1:5000/admin/dashboard?utm_source=gemini)

📖 Tutorial Singkat

## 👤 Sisi User (Tanpa Login)

- 1. Buka halaman utama aplikasi.

- 2. Pilih kategori ruangan dan klik "Pilih Paket".

- 3. Klik "Book Now", isi data diri, dan upload bukti transfer.

- 4. Klik "Kirim Pesanan" dan simpan kode booking Anda.

🔐 Sisi Admin


- 1. Buka halaman admin dan login (admin@conco.id / admin123).

- 2. Gunakan Dashboard untuk melihat statistik.

- 3. Gunakan menu Kelola Pesanan untuk mengubah status pesanan (Pending/Sukses/Batal).

- 4. Gunakan menu Kelola Ruangan untuk menambah atau mengedit ruangan.
