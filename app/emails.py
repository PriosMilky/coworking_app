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
        # Subject dinamis sesuai status
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
    # Username: coco + 4 digit terakhir kode booking
    # Contoh: BKG-2026-A1B2C3 → coco-B2C3
    suffix = kode_booking.replace('-', '')[-4:]
    username = f"coco-{suffix}"
    
    # Password: random 8 karakter
    import random
    import string
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    
    return username, password