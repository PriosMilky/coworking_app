import random
import string
import requests
from flask import render_template, current_app
from flask_mail import Message
from app import mail


def kirim_email_booking_success(booking):
    """Kirim email konfirmasi booking ke user."""
    try:
        msg = Message(
            subject=f'✅ Booking Berhasil - {booking.kode_booking}',
            recipients=[booking.email]
        )
        msg.html = render_template('email/booking_success.html', booking=booking)
        mail.send(msg)
        print(f"📧 Email booking terkirim ke {booking.email}")
        return True
    except Exception as e:
        print(f"❌ Gagal kirim email booking: {e}")
        return False


def kirim_email_status_update(booking):
    """Kirim email update status ke user (Sukses/Batal)."""
    try:
        if booking.status == 'sukses':
            subject = f'🎉 Booking Anda Disetujui - {booking.kode_booking}'
        elif booking.status == 'batal':
            subject = f'❌ Booking Dibatalkan - {booking.kode_booking}'
        else:
            subject = f'📋 Update Status Booking - {booking.kode_booking}'
        
        msg = Message(subject=subject, recipients=[booking.email])
        msg.html = render_template('email/status_update.html', booking=booking)
        mail.send(msg)
        print(f"📧 Email update status terkirim ke {booking.email}")
        return True
    except Exception as e:
        print(f"❌ Gagal kirim email update: {e}")
        return False


def generate_wifi_credentials(kode_booking):
    """Generate username & password WiFi dari kode booking."""
    suffix = kode_booking.replace('-', '')[-4:]
    username = f"coco-{suffix}"
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return username, password


def export_to_sheet(booking):
    """Kirim data booking ke Google Sheet via Apps Script Webhook."""
    try:
        webhook_url = current_app.config.get('GOOGLE_SHEET_WEBHOOK_URL')
        
        if not webhook_url or 'GANTI_URL' in webhook_url:
            print("⚠️ GOOGLE_SHEET_WEBHOOK_URL belum dikonfigurasi. Skip export.")
            return False
        
        data = {
            'tanggal_booking': booking.created_at.strftime('%Y-%m-%d %H:%M:%S') if booking.created_at else '-',
            'kode_booking': booking.kode_booking,
            'nama': booking.nama_lengkap,
            'email': booking.email,
            'no_whatsapp': booking.no_whatsapp or '-',
            'ruangan': booking.space.nama_ruangan,
            'tanggal_mulai': booking.tanggal_mulai.strftime('%Y-%m-%d'),
            'durasi': f"{booking.durasi} {booking.space.durasi_satuan}",
            'total_harga': booking.total_harga,
            'status': booking.status.upper()
        }
        
        response = requests.post(
            webhook_url,
            json=data,
            timeout=10,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"📊 Sheet export: {result.get('status')} (row {result.get('row')})")
            return True
        else:
            print(f"❌ Sheet export gagal: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Sheet export error: {e}")
        return False